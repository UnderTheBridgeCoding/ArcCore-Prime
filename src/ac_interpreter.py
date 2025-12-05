# ============================================================
# ARC INTERPRETER ENGINE — ArcCore-Prime V1
# Loop 6.B — Structural Reconstruction Integration
# Guardian: Arien
# ============================================================

from arc_guardian import ArcGuardian
from arc_prime import ArcMemorySystem
from ac_sigils import SigilEngine
from ac_collapse import ACCollapseEngine
from ac_reconstruct import ArcReconstruct


class ArcInterpreter:
    """
    The Interpreter transforms cleaned user commands into
    validated internal ArcCore actions.

    Now extended with:
      - ac reconstruct
      - ac thread <cycle>
      - ac summary

    Implements Cycle 12 (Interpreter Logic)
    and Cycle 31/33 (Reconstruction Pathways)
    """

    def __init__(self):
        self.guardian = ArcGuardian()
        self.memory = ArcMemorySystem()
        self.sigil = SigilEngine()
        self.collapse = ACCollapseEngine()
        self.reconstruct = ArcReconstruct()

        # Routing table (Expanded Command Set)
        self.routes = {
            # Memory inspection
            "walk": self.cmd_walk,
            "export": self.cmd_export,

            # Interaction insertion
            "inject": self.cmd_inject,

            # Sigils
            "sigil": self.cmd_sigil_test,

            # Guardian diagnostics
            "guardian": self.cmd_guardian_status,

            # Reconstruction engine
            "reconstruct": self.cmd_reconstruct_full,
            "thread": self.cmd_reconstruct_thread,
            "summary": self.cmd_summary,

            # Placeholder collapse/seed/prune
            "collapse": self.cmd_collapse,
        }

    # ============================================================
    # PARSE INTENT
    # ============================================================

    def parse_intent(self, text: str):
        parts = text.split(" ", 2)
        if len(parts) < 2:
            return None, None
        cmd = parts[1].strip()
        args = parts[2] if len(parts) >= 3 else ""
        return cmd, args

    # ============================================================
    # INTERPRET → ROUTE
    # ============================================================

    def interpret(self, cleaned: str):
        if not self.guardian.gate(cleaned):
            return "[Guardian] Command blocked."

        cmd, args = self.parse_intent(cleaned)
        if cmd is None:
            return "[Interpreter] Invalid command."

        if not self.guardian.validate_intent(cmd):
            return f"[Guardian] Intent '{cmd}' is not permitted."

        handler = self.routes.get(cmd)
        if handler is None:
            return f"[Interpreter] Unknown command '{cmd}'."

        try:
            return handler(args)
        except Exception as e:
            return f"[Interpreter Error] {str(e)}"

    # ============================================================
    # COMMAND HANDLERS
    # ============================================================

    def cmd_walk(self, args: str):
        return self.memory.load_and_inject()

    def cmd_export(self, args: str):
        self.memory.save_memory()
        return "[export] Memory saved."

    def cmd_inject(self, args: str):
        try:
            parts = args.split("|")
            if len(parts) != 3:
                return "[inject] Format: ac inject user|ai|cycle"
            user_text = parts[0].strip()
            ai_text = parts[1].strip()
            cycle_context = int(parts[2].strip())
            self.memory.ingest_interaction(user_text, ai_text, cycle_context)
            return "[inject] Interaction added."
        except Exception as e:
            return f"[inject error] {str(e)}"

    def cmd_sigil_test(self, args: str):
        score = self.sigil.evaluate(args)
        return f"[sigil] Priority = {score}"

    def cmd_guardian_status(self, args: str):
        return self.guardian.status_report()

    def cmd_collapse(self, args: str):
        return "[collapse] Collapse engine is active."

    # ============================================================
    # RECONSTRUCTION COMMANDS (Loop 6)
    # ============================================================

    def cmd_reconstruct_full(self, args: str):
        """Full structural reconstruction of the entire tree."""
        tree = self.memory.root.to_dict()
        return self.reconstruct.reconstruct_full(tree)

    def cmd_reconstruct_thread(self, args: str):
        """Reconstruct only the nodes belonging to a specific cycle."""
        if not args.strip():
            return "[thread] Usage: ac thread <cycle>"
        try:
            cycle_id = int(args.strip())
            tree = self.memory.root.to_dict()
            lines = self.reconstruct.reconstruct_thread(tree, cycle_id)
            return "\n".join(lines) if lines else "[thread] No entries found."
        except:
            return "[thread] Invalid cycle ID."

    def cmd_summary(self, args: str):
        """High-level reconstruction summary."""
        tree = self.memory.root.to_dict()
        lines = self.reconstruct.reconstruct_path(tree, depth=0)
        return "\n".join(lines)
