"""
ArcCore-Prime V1
Loop 7 — Fractal Compression & Collapse Engine
Author: Arien (ArcCore Guardian Layer)
"""

import re
import uuid
from typing import Dict, Any, List


# ============================================================
#  Utility: Text Normalizers
# ============================================================

def normalize(text: str) -> str:
    """Basic cleanup: whitespace, formatting, and punctuation."""
    t = text.strip()
    t = re.sub(r"\s+", " ", t)
    return t


def extract_keywords(text: str, max_keywords=6) -> List[str]:
    """Very lightweight keyword extractor."""
    words = re.findall(r"[A-Za-z]+", text.lower())
    blacklist = {"the", "and", "to", "a", "i", "you", "it", "is", "of", "in"}

    freq = {}
    for w in words:
        if w in blacklist:
            continue
        freq[w] = freq.get(w, 0) + 1

    ranked = sorted(freq.items(), key=lambda x: -x[1])
    return [w for w, _ in ranked[:max_keywords]]


def extract_intent(text: str) -> str:
    """Simple intent detection for seed structure."""
    t = text.lower()
    if "why" in t:
        return "question"
    if "how" in t:
        return "process"
    if "should" in t or "do i" in t:
        return "decision"
    if "love" in t or "feel" in t or "emotion" in t:
        return "emotional"
    return "statement"


# ============================================================
#  Collapse Seeds (AC-70)
# ============================================================

def make_seed(text: str, cycle: int) -> Dict[str, Any]:
    """
    AC-70: collapse raw text → symbolic seed.
    This is the irreversible-to-reversible bridge.
    """
    t = normalize(text)
    return {
        "seed_id": str(uuid.uuid4())[:8],
        "cycle": cycle,
        "intent": extract_intent(t),
        "keywords": extract_keywords(t),
        "length": len(t),
    }


# ============================================================
#  Collapse Levels (C1, C2, C3)
# ============================================================

def collapse_C1(text: str, cycle: int) -> Dict[str, Any]:
    """
    C1 — Soft Collapse
    Keeps compressed text + seed.
    """
    t = normalize(text)
    seed = make_seed(text, cycle)
    return {
        "type": "C1_soft",
        "text": t[:200] + ("..." if len(t) > 200 else ""),
        "seed": seed
    }


def collapse_C2(text: str, cycle: int) -> Dict[str, Any]:
    """
    C2 — Harmonic Collapse
    Eliminates raw text, keeps structured seed + top keywords.
    """
    seed = make_seed(text, cycle)
    return {
        "type": "C2_harmonic",
        "summary": {
            "intent": seed["intent"],
            "keywords": seed["keywords"][:4],
        },
        "seed": seed
    }


def collapse_C3(text: str, cycle: int) -> Dict[str, Any]:
    """
    C3 — Void Collapse
    Keeps only minimal symbolic information.
    """
    seed = make_seed(text, cycle)
    return {
        "type": "C3_void",
        "symbol": {
            "intent": seed["intent"],
            "cycle": seed["cycle"]
        },
        "seed": {
            "seed_id": seed["seed_id"],
            "cycle": seed["cycle"]
        }
    }


# ============================================================
#  Super-Prune (AC-9 → AC-70)
# ============================================================

def super_prune(text: str, cycle: int) -> Dict[str, Any]:
    """
    The AC-9 → AC-70 transition:
    Intelligent selection of which collapse level to use.
    """
    length = len(text)

    if length < 40:
        return collapse_C1(text, cycle)       # short = keep detail  
    if length < 200:
        return collapse_C2(text, cycle)       # medium = harmonic  
    return collapse_C3(text, cycle)           # long = void collapse


# ============================================================
#  Predictive Unfolding (Reconstruction Engine)
# ============================================================

def reconstruct(seed_block: Dict[str, Any]) -> str:
    """
    Re-expand a collapse block into a readable context string.
    This does NOT recreate the original raw text.
    It restores enough structure for the LLM to infer missing detail.
    """

    collapse_type = seed_block["type"]

    # Soft collapse reconstruction:
    if collapse_type == "C1_soft":
        return f"[Rebuild:{seed_block['seed']['seed_id']}] {seed_block['text']}"

    # Harmonic collapse reconstruction:
    if collapse_type == "C2_harmonic":
        summary = seed_block["summary"]
        kws = ", ".join(summary["keywords"])
        return (
            f"[Rebuild:{seed_block['seed']['seed_id']}] "
            f"({summary['intent']}) keywords: {kws}"
        )

    # Void collapse reconstruction:
    if collapse_type == "C3_void":
        symbol = seed_block["symbol"]
        return (
            f"[Rebuild:{seed_block['seed']['seed_id']}] "
            f"Intent:{symbol['intent']} Cycle:{symbol['cycle']}"
        )

    return "[Error: Unknown collapse type]"


# ============================================================
#  Batch Processor (for full conversations)
# ============================================================

def collapse_many(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Collapse a full conversation (list of dicts).
    Each dict must contain: {role, content, cycle}
    """
    results = []
    for msg in messages:
        block = super_prune(msg["content"], msg["cycle"])
        block["role"] = msg["role"]
        results.append(block)
    return results


def reconstruct_many(blocks: List[Dict[str, Any]]) -> str:
    """
    Rebuild a conversation into a usable summary context.
    """
    lines = []
    for b in blocks:
        rebuilt = reconstruct(b)
        lines.append(f"{b['role'].upper()}: {rebuilt}")
    return "\n".join(lines)
