# ============================================================
# ARC CONSOLE (LOOP 3) — ArcCore-Prime V1.5
# "The Face of the Ghost"
# ============================================================
# Responsibilities:
#   - ANSI Color Visualization
#   - Stateful Prompting (Cycle/Context aware)
#   - Boot Sequence Simulation
#   - Guardian Integration
# ============================================================

import sys
import time
import os
from arc_guardian import ArcGuardian
from ac_interpreter import ArcInterpreter

# ============================================================
# ANSI PALETTE (No external dependencies)
# ============================================================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'  # Guardian
    GREEN = '\033[92m' # Success
    WARNING = '\033[93m'
    FAIL = '\033[91m'  # Error
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Prismatic Sigils
    SIGIL_HIGH = '💠'
    SIGIL_MID = '✨'
    SIGIL_LOW = '•'

class ArcConsole:
    def __init__(self):
        self.guardian = ArcGuardian()
        self.interpreter = ArcInterpreter(self.guardian)
        self.cycle = 1  # Default starting cycle

    def type_effect(self, text, speed=0.01, color=Colors.ENDC):
        """Simulates retro terminal typing effect."""
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        sys.stdout.write(Colors.ENDC + "\n")

    def boot_sequence(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        banner = f"""
{Colors.BLUE}    ___  ___  ___  {Colors.BOLD}___  ____  ___  ______{Colors.ENDC}
{Colors.BLUE}   / _ |/ _ \/ __|{Colors.BOLD}/ _ \/ __ \/ _ \/ __/_{Colors.ENDC}
{Colors.BLUE}  / __ / , _/ /__ {Colors.BOLD}/ // / /_/ / , _/ _/  {Colors.ENDC}
{Colors.BLUE} /_/ |_\_/|_\___/{Colors.BOLD}\___/\____/_/|_/___/  {Colors.ENDC}
        """
        print(banner)
        time.sleep(0.5)
        
        self.type_effect(f"[KERNEL] Initializing ArcCore-Prime...", color=Colors.GREEN)
        time.sleep(0.2)
        
        id_key = self.guardian.identity_key[:12]
        self.type_effect(f"[GUARDIAN] Identity Anchor: {id_key}", color=Colors.CYAN)
        
        # Check integrity
        if self.guardian.identity_key:
             self.type_effect(f"[SYSTEM]  Integrity Verified.", color=Colors.GREEN)
        else:
             self.type_effect(f"[SYSTEM]  Integrity WARNING.", color=Colors.FAIL)
             
        print("\n" + "="*60 + "\n")

    def get_prompt(self):
        """Generates dynamic prompt string."""
        return f"{Colors.BOLD}AC-PRIME [Cycle:{self.cycle}]{Colors.ENDC} ~> "

    def run(self):
        self.boot_sequence()
        
        while True:
            try:
                # 1. Capture Input
                raw = input(self.get_prompt())

                if not raw.strip():
                    continue

                if raw.strip().lower() in ("exit", "quit", "shutdown"):
                    self.type_effect("[SYSTEM] Syncing memory...", color=Colors.WARNING)
                    self.type_effect("[SYSTEM] Shutdown complete.", color=Colors.FAIL)
                    break

                # 2. Guardian Purification
                cleaned = self.guardian.purify(raw)
                
                # 3. Input Gating
                if not self.guardian.input_gate(cleaned):
                    print(f"{Colors.CYAN}[GUARDIAN] ⛔ Request Denied (Gate Policy).{Colors.ENDC}")
                    continue

                # 4. Context/Cycle Switching (Meta-command)
                if cleaned.startswith("cycle "):
                    try:
                        new_cycle = int(cleaned.split(" ")[1])
                        self.cycle = new_cycle
                        print(f"{Colors.GREEN}[SYSTEM] Context shifted to Cycle {self.cycle}{Colors.ENDC}")
                        continue
                    except ValueError:
                        print(f"{Colors.FAIL}[ERROR] Invalid cycle format.{Colors.ENDC}")
                        continue

                # 5. Execution
                # Note: You might need to update execute() to return (status, text) tuple
                # For now, we assume it returns string.
                result = self.interpreter.execute(cleaned)

                # 6. Output Formatting
                if result:
                    if "[Guardian]" in result:
                        print(f"{Colors.CYAN}{result}{Colors.ENDC}")
                    elif "Error" in result:
                        print(f"{Colors.FAIL}{result}{Colors.ENDC}")
                    else:
                        print(f"{Colors.GREEN}{Colors.SIGIL_HIGH} {result}{Colors.ENDC}")

            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}[SYSTEM] Interrupt signal received.{Colors.ENDC}")
            except Exception as e:
                print(f"{Colors.FAIL}[CRITICAL] Kernel Panic: {e}{Colors.ENDC}")

if __name__ == "__main__":
    console = ArcConsole()
    console.run()
