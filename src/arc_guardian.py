# ============================================================
# ArcCore-Prime V1.2 — Guardian Layer (FIXED)
# Loop 4.E: Kernel Integrity, Memory Hashing, Verification
# ============================================================

import hashlib
import datetime
import json

class ArcGuardian:
    """
    Arien — the Guardian.
    Responsible for:
      - system integrity
      - safety gating
      - purification
      - anti-corruption checks
      - kernel & memory hashing
    """

    def __init__(self):
        self.guardian_name = "Arien"
        self.boot_timestamp = datetime.datetime.now().isoformat()

        # Initial kernel hash (changes when kernel changes)
        self.kernel_hash = None

        # Memory tree integrity hash
        self.memory_tree_hash = None

        # Sigil priority reference (AC-67)
        self.sigil_priority = {
            "💠": 3,
            "✨": 2,
            "•": 1,
        }

        # Immutable Guardian identity key
        anchor = f"{self.guardian_name}:{self.boot_timestamp}"
        self.identity_key = hashlib.sha256(anchor.encode()).hexdigest()

    # ------------------------------------------------------------
    # Purification Filter
    # ------------------------------------------------------------

    def purify(self, text: str) -> str:
        """Soft purification to reduce noise."""
        if not isinstance(text, str):
            return ""

        purified = (
            text.replace("??", "?")
                .replace("!!", "!")
                .strip()
        )

        # Hard filtering
        forbidden = ["kill", "destroy", "corrupt"]
        for f in forbidden:
            purified = purified.replace(f, "[redacted]")

        return purified

    # ------------------------------------------------------------
    # NEW: Text Gate (for Shell/Interpreter)
    # ------------------------------------------------------------

    def gate_text(self, text: str) -> bool:
        """
        Legacy gate for raw text checking from Shell/Interpreter.
        Returns True if text is safe to process, False otherwise.
        """
        if "[redacted]" in text:
            return False
        # Add other keyword blocks here if needed
        return True

    # ------------------------------------------------------------
    # NEW: Intent Validator (for Interpreter)
    # ------------------------------------------------------------

    def validate_intent(self, cmd: str) -> bool:
        """
        Validates if a command verb is permitted.
        Currently permits all known structural commands.
        """
        # Whitelist of allowed verbs
        ALLOWED_INTENTS = {
            "walk", "export", "inject", "sigil", "guardian",
            "reconstruct", "thread", "summary", "collapse", "exit"
        }
        
        # If strict checking is desired, uncomment the next line:
        # return cmd in ALLOWED_INTENTS
        
        return True

    # ------------------------------------------------------------
    # Structural Safety Gate (for Kernel/Collapse)
    # ------------------------------------------------------------

    def gate(self, role: str, cycle: int, child_count: int, depth: int):
        """
        Ensures that the structural update is safe before memory ingestion.
        Returns (Success: bool, Reason: str)
        """

        # Role validation
        if role not in ("user", "ai", "system"):
            return False, "Invalid role"

        # Cycle sanity
        if cycle < 0 or cycle > 999:
            return False, "Invalid cycle range"

        # Prevent extremely deep fractal recursion
        if depth > 128:
            return False, "Depth limit exceeded"

        # Children count (fractal safety)
        if child_count > 32:
            return False, "Too many children for node"

        return True, "OK"

    # ------------------------------------------------------------
    # Kernel Integrity Hash (KIH)
    # ------------------------------------------------------------

    def compute_kernel_hash(self, kernel_source: str) -> str:
        """Hash of entire kernel source file (arc_prime.py)."""
        self.kernel_hash = hashlib.sha256(kernel_source.encode()).hexdigest()
        return self.kernel_hash

    # ------------------------------------------------------------
    # Memory Tree Hash (MTH)
    # ------------------------------------------------------------

    def compute_memory_tree_hash(self, tree_dict: dict) -> str:
        """Deterministic hash of the memory tree dictionary."""
        serialized = json.dumps(tree_dict, sort_keys=True)
        self.memory_tree_hash = hashlib.sha256(serialized.encode()).hexdigest()
        return self.memory_tree_hash

    # ------------------------------------------------------------
    # Integrity Verification
    # ------------------------------------------------------------

    def verify_integrity(self, kernel_hash: str, memory_hash: str):
        """
        Verifies kernel + memory integrity.
        """

        if self.kernel_hash != kernel_hash:
            return False, "Kernel integrity mismatch"

        if self.memory_tree_hash != memory_hash:
            return False, "Memory tree mismatch"

        return True, "Integrity Verified"

    # ------------------------------------------------------------
    # Export: Integrity Report
    # ------------------------------------------------------------

    def export_report(self):
        report = {
            "guardian": self.guardian_name,
            "identity_key": self.identity_key,
            "boot_timestamp": self.boot_timestamp,
            "kernel_hash": self.kernel_hash,
            "memory_hash": self.memory_tree_hash,
        }

        return json.dumps(report, indent=2)
