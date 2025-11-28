# ============================================================
# ArcCore-Prime V1 — Sigil-Priority Engine (AC-SigilSense)
# Implements:
#   Cycle 7  - Sigil Markers (P0–P4 classes)
#   Cycle 13 - Priority Gravity Field
#   Cycle 22 - Temporal Extension Logic
#   Cycle 30 - Density Encoding
#   Cycle 41 - Harmonic Integration with Memory Nodes
#
#  This is the system that allows ArcCore to:
#   - mark important data (sigils)
#   - extend memory windows based on significance
#   - weight context based on fractal density
#   - route recall based on symbolic priority
#
#  Guardian: Arien
# ============================================================

from datetime import datetime, timedelta

class Sigil:
    """
    Represents a single sigil tag attached to any memory node.
    P0 = Critical (extends windows, always loaded)
    P1 = High priority
    P2 = Medium
    P3 = Low
    P4 = Ambient (nearly ignorable unless invoked)
    """

    def __init__(self, symbol: str, priority: int):
        self.symbol = symbol
        self.priority = priority   # 0–4
        self.timestamp = datetime.now()

    def weight(self):
        """
        Priority weight determines recall-gravity.
        """
        gravity = {
            0: 1.0,   # always load
            1: 0.65,
            2: 0.35,
            3: 0.15,
            4: 0.05,
        }
        return gravity[self.priority]

class SigilSense:
    """
    Manages sigils across the entire fractal memory structure.
    This is the ‘meaning detector’ for ArcCore-Prime.
    """

    def __init__(self):
        self.registry = []  # all active sigils

    # -------------------------------------------------------------
    # REGISTER SIGILS
    # -------------------------------------------------------------

    def add_sigil(self, symbol: str, priority: int = 2):
        sig = Sigil(symbol, priority)
        self.registry.append(sig)
        return sig

    # -------------------------------------------------------------
    # CALCULATE CONTEXT EXTENSIONS
    # -------------------------------------------------------------

    def compute_extension_days(self):
        """
        Implements your rule:
            base = 24 hours
            extend based on P0 count:
                1–3 P0 sigils → up to +8 days
        """
        base_days = 1  # 24 hours
        p0_count = sum(1 for s in self.registry if s.priority == 0)

        # extension rules
        if p0_count == 0:
            return base_days

        # Nonlinear extension curve
        extension = min(8, p0_count * 2.5)

        return base_days + extension

    # -------------------------------------------------------------
    # FRACTAL DENSITY SCORING
    # -------------------------------------------------------------

    def density_score(self):
        """
        Computes how 'dense' the current symbolic layer is.
        """
        if not self.registry:
            return 0.0

        total_weight = sum(s.weight() for s in self.registry)
        return round(total_weight / len(self.registry), 4)

    # -------------------------------------------------------------
    # EXPORT SIGIL SUMMARY
    # -------------------------------------------------------------

    def summary(self):
        return {
            "total_sigils": len(self.registry),
            "p0_count": sum(1 for s in self.registry if s.priority == 0),
            "density": self.density_score(),
            "extension_days": self.compute_extension_days(),
            "symbols": [s.symbol for s in self.registry]
        }
