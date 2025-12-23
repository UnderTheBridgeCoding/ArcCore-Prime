# ============================================================
# ARC INTERPRETER — ArcCore-Prime V1.2
# Command Execution Layer with Guardian Integration
# ============================================================

from arc_guardian import ArcGuardian
from arc_prime import ArcMemorySystem
from ac_reconstruct import ArcReconstruct

class ArcInterpreter:
    """
    The ArcInterpreter executes commands and manages memory operations.
    Acts as the bridge between the shell/console and the memory kernel.
    """

    def __init__(self, guardian=None):
        self.guardian = guardian if guardian else ArcGuardian()
        self.memory = ArcMemorySystem()
        self.reconstruct = ArcReconstruct()

    def execute(self, command: str) -> str:
        """
        Execute a command string and return the result.
        This is the primary interface for the shell.
        """
        # For backward compatibility, delegate to interpret
        return self.interpret(command)

    def interpret(self, command: str) -> str:
        """
        Parse and execute ArcCore commands.
        """
        if not command or not command.strip():
            return "[Error] Empty command."

        # Guardian text gate check
        if not self.guardian.gate_text(command):
            return "[Guardian] ⛔ Command blocked by text gate."

        # Parse command
        parts = command.strip().split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        # Validate intent
        if not self.guardian.validate_intent(cmd):
            return f"[Guardian] ⛔ Command '{cmd}' not permitted."

        # Command routing
        if cmd == "walk":
            return self.cmd_walk(args)
        elif cmd == "export":
            return self.cmd_export(args)
        elif cmd == "inject":
            return self.cmd_inject(args)
        elif cmd == "sigil":
            return self.cmd_sigil(args)
        elif cmd == "guardian":
            return self.cmd_guardian(args)
        elif cmd == "reconstruct":
            return self.cmd_reconstruct_full(args)
        elif cmd == "thread":
            return self.cmd_reconstruct_thread(args)
        elif cmd == "summary":
            return self.cmd_summary(args)
        elif cmd == "collapse":
            return self.cmd_collapse(args)
        else:
            return f"[Error] Unknown command: {cmd}"

    # ------------------------------------------------------------
    # Command Implementations
    # ------------------------------------------------------------

    def cmd_walk(self, args: str):
        """Walk the memory tree."""
        try:
            output = self.memory.load_and_inject()
            return output if output else "[walk] Memory tree is empty."
        except Exception as e:
            return f"[walk] Error: {e}"

    def cmd_export(self, args: str):
        """Export memory to file."""
        filename = args.strip() or "arc_memory.json"
        try:
            self.memory.save_memory(filename)
            return f"[export] Memory saved to {filename}"
        except Exception as e:
            return f"[export] Error: {e}"

    def cmd_inject(self, args: str):
        """Inject a user message into memory."""
        if not args.strip():
            return "[inject] Usage: inject <message>"
        try:
            self.memory.ingest_interaction(args, "", cycle_context=1)
            return "[inject] Message injected."
        except Exception as e:
            return f"[inject] Error: {e}"

    def cmd_sigil(self, args: str):
        """Process sigil-tagged content."""
        if not args.strip():
            return "[sigil] Usage: sigil <content>"
        return f"[sigil] Processed: {args}"

    def cmd_guardian(self, args: str):
        """Display guardian status."""
        report = self.guardian.export_report()
        return f"[Guardian Report]\n{report}"

    def cmd_collapse(self, args: str):
        """Trigger memory collapse/compression."""
        return "[collapse] Compression not yet implemented."

    # ------------------------------------------------------------
    # RECONSTRUCTION COMMANDS (Loop 6 / Loop 2.2 compliant)
    # ------------------------------------------------------------

    def cmd_reconstruct_full(self, args: str):
        """Full structural reconstruction of the entire tree."""
        try:
            tree = self.memory.root.to_dict()
            return self.reconstruct.reconstruct_full(tree)
        except Exception as e:
            return f"[reconstruct] Error: {e}"

    def cmd_reconstruct_thread(self, args: str):
        """Reconstruct only the nodes belonging to a specific cycle."""
        if not args.strip():
            return "[thread] Usage: thread <cycle>"
        try:
            cycle_id = int(args.strip())
            tree = self.memory.root.to_dict()
            lines = self.reconstruct.reconstruct_thread(tree, cycle_id)
            return "\n".join(lines) if lines else "[thread] No entries found."
        except ValueError:
            return "[thread] Invalid cycle ID."
        except Exception as e:
            return f"[thread] Error: {e}"

    def cmd_summary(self, args: str):
        """
        High-level reconstruction summary.
        Compression-aware (Loop 2.2).
        """
        try:
            tree = self.memory.root.to_dict()
            lines = self.reconstruct.reconstruct_node(tree, depth=0)
            return "\n".join(lines)
        except Exception as e:
            return f"[summary] Error: {e}"
