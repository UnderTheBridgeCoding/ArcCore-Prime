# ============================================================
# ARC RECONSTRUCTION ENGINE — ArcCore-Prime V1
# Loop 6 — Structural Reconstruction
# Loop 2.2 — Compression-Aware Reconstruction
# Guardian: Arien
# ============================================================

from typing import List, Dict, Any
from ac_collapse import CompressionLevel


class ArcReconstruct:
    """
    Deterministic reconstruction engine for ArcCore-Prime.

    Responsibilities:
      - Walk structural paths in the memory tree
      - Rebuild multi-node meaning from seeds
      - Create threads (cycle-sorted or path-sorted)
      - Generate readable reconstructed output
      - Respect compression fidelity (Loop 2.2)
    """

    # ------------------------------------------------------------
    # SEED EXPANSION (deterministic)
    # ------------------------------------------------------------

    def expand_seed(self, seed: str) -> str:
        """
        Deterministic seed expansion:
        Converts a compressed seed into a richer contextual statement.
        Uses structural logic, not generative models.
        """
        if seed is None:
            return "(no seed)"

        if seed.startswith("[AC-"):
            cycle_tag = seed.split("]")[0][1:]
            body = seed.split("] ", 1)[-1]
            return f"({cycle_tag}) → {body}"

        if seed.startswith("[Seed AC-"):
            cycle_tag = seed.split("]")[0][1:]
            body = seed.split("]: ", 1)[-1]
            return f"({cycle_tag}) → {body}"

        return f"(expanded) {seed}"

    # ------------------------------------------------------------
    # PATH-BASED RECONSTRUCTION (RAW / SUMMARY)
    # ------------------------------------------------------------

    def reconstruct_path(self, node: Dict[str, Any], depth: int = 0) -> List[str]:
        """
        Reconstructs a node and its children structurally.
        Used for RAW and SUMMARY compression levels.
        """
        output = []
        indent = "  " * depth

        seed = node.get("seed") or node.get("content")
        expanded = self.expand_seed(seed)
        cycle = node.get("cycle")
        role = node.get("role", "").upper()

        output.append(f"{indent}[AC-{cycle}] {role}: {expanded}")

        for child in node.get("children", []):
            output.extend(self.reconstruct_node(child, depth + 1))

        return output

    # ------------------------------------------------------------
    # CYCLE-BASED THREAD RECONSTRUCTION
    # ------------------------------------------------------------

    def reconstruct_thread(self, tree: Dict[str, Any], cycle_id: int) -> List[str]:
        """
        Returns all nodes belonging to a given cycle, expanded.
        Compression level is respected per node.
        """
        results = []

        def walk(n: Dict[str, Any]):
            if int(n.get("cycle", -1)) == cycle_id:
                results.extend(self.reconstruct_node(n))

            for child in n.get("children", []):
                walk(child)

        walk(tree)
        return results

    # ------------------------------------------------------------
    # COMPRESSION-AWARE DISPATCH (Loop 2.2)
    # ------------------------------------------------------------

    def reconstruct_node(self, node: Dict[str, Any], depth: int = 0) -> List[str]:
        """
        Dispatch reconstruction based on compression level.
        Reconstruction is meaning-first and fidelity-honest.
        """

        level = node.get("compression_level", CompressionLevel.RAW)
        indent = "  " * depth
        role = node.get("role", "").upper()
        cycle = node.get("cycle")

        # RAW and SUMMARY — full structural traversal
        if level in (CompressionLevel.RAW, CompressionLevel.SUMMARY):
            return self.reconstruct_path(node, depth)

        # SEED — expand auric seed only
        if level == CompressionLevel.SEED:
            expanded = self.expand_seed(node.get("seed"))
            return [f"{indent}[AC-{cycle}] {role}: {expanded}"]

        # SIGIL_ONLY — honest boundary
        if level == CompressionLevel.SIGIL_ONLY:
            return [
                f"{indent}[AC-{cycle}] {role}: "
                "[Sigil Anchor — reconstruction required]"
            ]

        # Defensive fallback
        return [f"{indent}[AC-{cycle}] {role}: [Unknown compression state]"]

    # ------------------------------------------------------------
    # FULL TREE RECONSTRUCTION (pretty print)
    # ------------------------------------------------------------

    def reconstruct_full(self, tree: Dict[str, Any]) -> str:
        """
        Reconstructs the entire tree into a human-readable
        structural summary, respecting compression levels.
        """
        lines = self.reconstruct_node(tree)
        return "\n".join(lines)
