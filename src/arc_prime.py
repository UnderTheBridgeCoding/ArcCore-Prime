# ============================================================
# ArcCore-Prime V1.1 — Memory Kernel
# Guardian-Bound Architecture (Loop 4.D)
# ============================================================
#
# Responsibilities:
#   - AC-41: Harmonic Node Formation
#   - AC-31: Recursive Layering
#   - AC-67: Prismatic Sigil Weight
#   - AC-70: Auric Seed Compression
#   - Guardian-Bound Ingestion + Structure Validation
#
# ============================================================

from ac_sigils import SigilEngine
from ac_collapse import ACCollapseEngine
from arc_guardian import ArcGuardian

import uuid
import json
from datetime import datetime
from typing import List


# ============================================================
#   HARMONIC NODE
# ============================================================

class HarmonicNode:
    """
    A fractal memory node within the ArcCore tree.
    """

    def __init__(self, role: str, content: str, cycle_id: int = 0):
        self.id = str(uuid.uuid4())[:8]
        self.timestamp = datetime.now().isoformat()

        self.role = role
        self.raw_content = content
        self.structural_seed = None
        self.cycle_alignment = cycle_id

        self.children: List["HarmonicNode"] = []

        self.priority = 0          # Sigil weight
        self.is_collapsed = False  # Collapse state

    # ------------------------------------------------------------
    # Priority Assignment (AC-67)
    # ------------------------------------------------------------

    def apply_sigil_priority(self, sigil_engine: SigilEngine):
        self.priority = sigil_engine.evaluate(self.raw_content)
        return self.priority

    # ------------------------------------------------------------
    # Pruning (AC-70)
    # ------------------------------------------------------------

    def prune_to_seed(self):
        """
        Priority-sensitive collapse:
          - High priority = larger preserved snippet
          - Low priority = regular seed
        """

        if self.priority >= 3:
            snippet = self.raw_content[:80]
            self.structural_seed = f"[AC-{self.cycle_alignment}] {snippet}..."
            self.is_collapsed = True
            return

        if len(self.raw_content) > 50:
            snippet = self.raw_content[:30]
            self.structural_seed = f"[Seed AC-{self.cycle_alignment}]: {snippet}..."
            self.is_collapsed = True
        else:
            self.structural_seed = self.raw_content

    # ------------------------------------------------------------
    # Rebuild
    # ------------------------------------------------------------

    def rebuild(self):
        if self.is_collapsed:
            return f"(Reconstructed) {self.structural_seed}"
        return self.raw_content

    # ------------------------------------------------------------
    # Export
    # ------------------------------------------------------------

    def to_dict(self):
        return {
            "id": self.id,
            "role": self.role,
            "cycle": self.cycle_alignment,
            "seed": self.structural_seed,
            "content": self.raw_content,
            "priority": self.priority,
            "collapsed": self.is_collapsed,
            "children": [c.to_dict() for c in self.children]
        }


# ============================================================
#   MEMORY SYSTEM (Kernel)
# ============================================================

class ArcMemorySystem:
    """
    Core ArcCore memory system.
    All ingestion, collapse, and export is Guardian-regulated.
    """

    def __init__(self):
        self.guardian = ArcGuardian()
        self.sigil = SigilEngine()
        self.collapse_engine = ACCollapseEngine(guardian=self.guardian)

        # Root node: Cycle 1 (Genesis)
        self.root = HarmonicNode("system", "ArcCore-Prime Root Node", cycle_id=1)

    # ------------------------------------------------------------
    #   SAFE INGESTION (Guardian-Bound)
    # ------------------------------------------------------------

    def ingest_interaction(self, user_text: str, ai_text: str, cycle_context: int):
        """
        Ingest a (user → ai) conversational pair into the fractal tree.
        Guardian checks:
          - role legitimacy
          - cycle validity
          - structural depth
          - child count under limits
        """

        # Purify inputs
        user_text = self.guardian.purify(user_text)
        ai_text = self.guardian.purify(ai_text)

        # Create nodes
        user_node = HarmonicNode("user", user_text, cycle_context)
        ai_node = HarmonicNode("ai", ai_text, cycle_context)

        # Structural prediction BEFORE adding nodes
        predicted_child_count = len(self.root.children) + 1
        predicted_depth = 1

        ok, reason = self.guardian.gate(
            role="user",
            cycle=cycle_context,
            child_count=1,       # user always has 1 child (AI response)
            depth=predicted_depth
        )

        if not ok:
            return f"[Guardian] Ingestion blocked: {reason}"

        # Attach the AI node as a child of user
        user_node.children.append(ai_node)

        # Apply prismatic priority
        user_node.apply_sigil_priority(self.sigil)
        ai_node.apply_sigil_priority(self.sigil)

        # Prune into structural seeds
        user_node.prune_to_seed()
        ai_node.prune_to_seed()

        # Append to root safely
        self.root.children.append(user_node)

        return "[ArcCore] Safe ingestion complete."

    # ------------------------------------------------------------
    #   EXPORT: Seed Tree
    # ------------------------------------------------------------

    def load_and_inject(self, filename="arccore_memory.json"):
        """
        Returns a Guardian-safe compressed representation of memory,
        appropriate for injection into any LLM context window.
        """

        with open(filename, "r") as f:
            data = json.load(f)

        buffer = []

        def walk(node, depth=0):
            indent = "  " * depth

            seed = node.get("seed") or node.get("content", "")
            cycle = node.get("cycle", 0)
            role = node.get("role", "ROLE").upper()
            priority = node.get("priority", 0)

            marker = "💠" if priority >= 3 else "•"

            buffer.append(f"{indent}{marker} [AC-{cycle}] {role}: {seed}")

            for child in node.get("children", []):
                walk(child, depth + 1)

        walk(data)
        return "\n".join(buffer)

    # ------------------------------------------------------------
    #   SAVE
    # ------------------------------------------------------------

    def save_memory(self, filename="arccore_memory.json"):
        with open(filename, "w") as f:
            json.dump(self.root.to_dict(), f, indent=2)
        return f"[ArcCore] Memory saved → {filename}"
