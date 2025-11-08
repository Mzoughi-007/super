from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import subprocess
import time

console = Console()

options = {
    "1": ("Time-Desynchronization Attacks", ["4.Time-Desynchronization-Attacks/timestamp_simulator.py"]),
    "2": ("Cryogenic System Exploits", ["6.-Cryogenic-System-Exploits/cryo_simulator.py"]),
    "3": ("Relay Satellite Hijack / Orbital Spoofing", ["Relay-Satellite-Hijack-Orbital-Spoofing-/Satelite_check.py"]),
    "4": ("Biological Payload Manipulation", ["5.-Biological-Payload-Manipulation/life_support_command.py"]),
    "5": ("Cosmic Bit Flip", ["COSMIC_BIT_FLIP/spacecraft.py", "COSMIC_BIT_FLIP/radiation_node.py", "COSMIC_BIT_FLIP/earth.py"]),
    "6": ("Wormhole Communications", ["Wormhole/spacecraft.py", "Wormhole/relay.py", "Wormhole/earth.py"])
}


def run_option(files, interactive=False):
    """
    Run files sequentially:
    - spacecraft.py & radiation_node.py in background
    - earth.py interactively
    - menu returns after all finish
    """
    procs = []

    try:
        for idx, f in enumerate(files):
            console.print("\n" + "="*60, style="bright_blue")
            console.print(f"🚀 Launching: [bold magenta]{f}[/bold magenta]", style="bright_cyan")
            console.print("="*60 + "\n", style="bright_blue")

            # Run the first two scripts in background
            if "COSMIC_BIT_FLIP" in f and idx < 2:
                p = subprocess.Popen(["python3", f])
                procs.append(p)
                console.print(f"[yellow]Running in background...[/yellow]")
                time.sleep(0.3)
                continue

            # Run earth.py interactively
            if interactive and "earth.py" in f:
                p = subprocess.Popen(
                    ["python3", f],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                try:
                    while True:
                        cmd = Prompt.ask("[yellow]Enter command to send (type 'exit' to finish)[/yellow]")
                        if cmd.strip().lower() == "exit" or cmd.strip() == "":
                            break
                        p.stdin.write(cmd + "\n")
                        p.stdin.flush()

                        # Read all available output from earth.py
                        while True:
                            line = p.stdout.readline()
                            if not line:
                                break
                            console.print(f"[cyan]{line.strip()}[/cyan]")

                    # Close stdin and wait for earth.py to exit
                    p.stdin.close()
                    p.wait()

                    # Print any remaining stdout
                    for line in p.stdout:
                        console.print(f"[cyan]{line.strip()}[/cyan]")
                    for line in p.stderr:
                        console.print(f"[red]{line.strip()}[/red]")

                except KeyboardInterrupt:
                    p.terminate()
            else:
                # Non-interactive scripts (other options)
                p = subprocess.Popen(["python3", f])
                p.wait()

            console.print("\n" + "-"*60, style="bright_green")
            console.print(f"✅ Completed: [bold magenta]{f}[/bold magenta]", style="bright_green")
            console.print("-"*60 + "\n", style="bright_green")
            time.sleep(0.2)

    finally:
        # Terminate background processes
        for p in procs:
            if p.poll() is None:
                p.terminate()
                console.print(f"[red]Background process terminated.[/red]")

    console.print("\n[green]🛸 All processes finished. Returning to menu 🛸[/green]\n")
    time.sleep(0.5)


def main():
    console.clear()
    console.print(Panel.fit("[bold cyan]🛰️  Securing Interplanetary Communications 🛰️[/bold cyan]"))

    while True:
        console.print("\n[bold yellow]Select an option:[/bold yellow]\n")
        for k, v in options.items():
            console.print(f"  [bold cyan]{k}[/bold cyan] - [italic white]{v[0]}[/italic white]")
        console.print("  [bold red]0[/bold red] - Exit\n")

        choice = Prompt.ask("[bold green]Select option[/bold green]", choices=[str(i) for i in range(7)])
        console.print("\n")

        if choice == "0":
            console.print(Panel.fit("[bold red]👋 Exiting... Safe travels![/bold red]"))
            break

        option_name = options[choice][0]
        console.print(Panel.fit(f"✨ Running [bold magenta]{option_name}[/bold magenta] demo ✨", style="bright_blue"))

        # Interactive only for earth.py in option 5 or 6
        interactive = False
        if choice in ["5", "6"]:
            interactive = True

        run_option(options[choice][1], interactive=interactive)

        console.print("\n[green]🛸 Processes finished, returning to menu 🛸[/green]\n")
        time.sleep(0.5)


if __name__ == "__main__":
    main()

