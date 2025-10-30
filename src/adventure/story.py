from adventure.utils import read_events_from_file
from rich.console import Console
from rich.prompt import Prompt
import random

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[bold green]You wake up in a dark forest. You can go left or right.[/bold green]")
    
    while True:
        choice = Prompt.ask(
            "[yellow]Which direction do you choose?[/yellow]",
            choices=["left", "right", "exit"]
        )
        choice = choice.strip().lower()

        if choice == "exit":
            console.print("[bold]You decide to exit the forest. Goodbye![/bold]")
            break

        console.print(step(choice, events))
