# ============================================================
# ARC SHELL — ArcCore-Prime V1
# Loop 5.E — Interpreter Integration
# Guardian: Arien
# ============================================================

from arc_guardian import ArcGuardian
from ac_interpreter import ArcInterpreter

import sys


class ArcShell:
    """
    The ArcShell is the IO layer of ArcCore-Prime.
    It handles:
        - raw string input
        - purification
        - passing commands to Interpreter
        - formatting output safely

    The Shell no longer performs any internal logic.
    All kernel operations run through ArcInterpreter.
    """

    def __init__(self):
        self.guardian = ArcGuardian()
        self.interpreter = ArcInterpreter()

    # ------------------------------------------------------------
    # CLEAN + ROUTE INPUT (Core Shell Logic)
    # ------------------------------------------------------------

    def process(self, text: str):
        """
        Full pipeline:
            1. Purification
            2. Guardian Precheck
            3. Forward to Interpreter
        """

        # 1. Purify text (removes noise)
        cleaned = self.guardian.purify(text)

        # 2. Gate the command string itself
        if not self.guardian.gate(cleaned):
            return "[Guardian] Command blocked for safety."

        # 3. Forward to Interpreter
        return self.interpreter.interpret(cleaned)

    # ------------------------------------------------------------
    # INTERACTIVE LOOP
    # ------------------------------------------------------------

    def run(self):
        print("ArcShell — ArcCore-Prime V1")
        print("Type 'exit' to quit.\n")

        while True:
            try:
                raw = input("ac> ").strip()

                if raw.lower() == "exit":
                    print("Exiting ArcShell.")
                    break

                if not raw:
                    continue

                result = self.process(raw)
                print(result)

            except KeyboardInterrupt:
                print("\nExiting ArcShell.")
                break

            except Exception as e:
                print(f"[ArcShell Error] {str(e)}")


# ============================================================
# Shell Runner
# ============================================================

if __name__ == "__main__":
    shell = ArcShell()
    shell.run()
