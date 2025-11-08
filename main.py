from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import subprocess
import time

console = Console()

options = {
    "1": ("Time-Desynchronization Attacks", ["4.Time-Desynchronization-Attacks/timestamp_simulator.py"]),
    "2": ("Cryogenic System Exploits", ["6.-Cryogenic-System-Exploits/cryo_security.py"]),
    "3": ("Relay Satellite Hijack / Orbital Spoofing", ["Relay-Satellite-Hijack-Orbital-Spoofing-/orbital_auth.py"]),
    "4": ("Biological Payload Manipulation", ["5.-Biological-Payload-Manipulation/biometric_auth.py"]),
    "5": ("Cosmic Bit Flip", ["COSMIC_BIT_FLIP/earth.py", "COSMIC_BIT_FLIP/spacecraft.py", "COSMIC_BIT_FLIP/radiation_node.py"]),
    "6": ("Wormhole Communications", ["Wormhole/spacecraft.py", "Wormhole/relay.py", "Wormhole/earth.py"])
}

def run_option(files, interactive=False):
    procs = []
    try:
        for f in files:
            if interactive:
                if "earth.py" in f:
                    msg = Prompt.ask("Enter command to send")
                    p = subprocess.Popen(["python3", f], stdin=subprocess.PIPE)
                    p.stdin.write(msg.encode() + b"\n")
                    p.stdin.flush()
                else:
                    p = subprocess.Popen(["python3", f])
            else:
                p = subprocess.Popen(["python3", f])
            procs.append(p)
        while any(p.poll() is None for p in procs):
            time.sleep(0.1)
    finally:
        for p in procs:
            if p.poll() is None:
                p.terminate()

def main():
    console.clear()
    console.print(Panel.fit("[bold cyan]Securing Interplanetary Communications[/bold cyan]"))
    while True:
        for k,v in options.items():
            console.print(f"[bold yellow]{k}[/bold yellow] - {v[0]}")
        console.print("[bold yellow]0[/bold yellow] - Exit")
        choice = Prompt.ask("Select option", choices=[str(i) for i in range(7)])
        if choice == "0":
            break
        if choice == "6":
            console.print("Running Wormhole Communications")
            run_option(options[choice][1], interactive=True)
        else:
            console.print(f"Running {options[choice][0]} demo")
            run_option(options[choice][1])
        console.print("[green]Processes finished, returning to menu[/green]")

if __name__=="__main__":
    main()

