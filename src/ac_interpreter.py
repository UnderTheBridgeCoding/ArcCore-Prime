# ============================================================
# RECONSTRUCTION COMMANDS (Loop 6 / Loop 2.2 compliant)
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
    """
    High-level reconstruction summary.
    Compression-aware (Loop 2.2).
    """
    tree = self.memory.root.to_dict()
    lines = self.reconstruct.reconstruct_node(tree, depth=0)
    return "\n".join(lines)
