# ============================================================
# ACCollapseEngine — Safe Collapse Engine
# ArcCore-Prime V1.4
# ============================================================

import copy

class ACCollapseEngine:
    """
    Converts full memory nodes into safe, compact structural seeds.
    """

    def collapse_state(self, node: dict) -> dict:
        """
        Performs safe pruning on any memory node dictionary.
        """

        collapse = copy.deepcopy(node)

        # Remove raw content if seed exists
        if collapse.get("seed"):
            collapse["content"] = None
        else:
            # fallback: generate seed
            raw = collapse.get("content", "")
            snippet = raw[:50]
            collapse["seed"] = f"[AutoSeed]: {snippet}..."

        # Collapse children recursively
        children = collapse.get("children", [])
        collapsed_children = []
        for c in children:
            collapsed_children.append(self.collapse_state(c))
        collapse["children"] = collapsed_children

        return collapse
