import json
from rich.console import Console
import typer
from typing_extensions import Annotated
import questionary
from prompt_toolkit.styles import Style


console = Console()

def get_tasks():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    return tasks


def commit(tasks, config_path="tasks.json"):
    with open(config_path, "w") as file:
        json.dump(tasks, file)


def add_task(tasks, task, status, notes):
    task_dict = {'name': task, 'status': status, 'notes': notes}

    tasks["tasks"].append(task_dict)

    commit(tasks)


def change_task(tasks, idx, task, status, notes):
    if task:
        tasks["tasks"][idx]["name"] = task
    if status:
        tasks["tasks"][idx]["status"] = status
    if notes:
        tasks["tasks"][idx]["notes"] = notes

    commit(tasks)


def remove_task(tasks, idx):
    tasks["tasks"].pop(idx)

    commit(tasks)

def list_tasks(tasks, nerd):
    task_list = tasks["tasks"]

    if nerd:
        for idx, task in enumerate(task_list):
            if task["status"] == "Complete":
                task_fmt = f"""[green]󰄳 {task["name"]}\n  {task["notes"]}[/green]"""

                console.print(task_fmt)
            elif task["status"] == "In Progress":
                task_fmt = f"""[yellow]󰄯 {task["name"]}\n  {task["notes"]}[/yellow]"""

                console.print(task_fmt)
            elif task["status"] == "Todo":
                task_fmt = f"""[bright_black]󰄰 {task["name"]}\n  {task["notes"]}[/bright_black]"""

                console.print(task_fmt)
    else:
        for idx, task in enumerate(task_list):
            if task["status"] == "Complete":
                task_fmt = f"""[green]◉ {task["name"]}\n  {task["notes"]}[/green]"""

                console.print(task_fmt)
            elif task["status"] == "In Progress":
                task_fmt = f"""[yellow]◐ {task["name"]}\n  {task["notes"]}[/yellow]"""

                console.print(task_fmt)
            elif task["status"] == "Todo":
                task_fmt = f"""[bright_black]◌ {task["name"]}\n  {task["notes"]}[/bright_black]"""

                console.print(task_fmt)

def main(nerd: Annotated[bool, typer.Option(help="Use Nerd Font glyphs")] = False, interactive: Annotated[bool, typer.Option(help="Use Nerd Font glyphs")] = False):
    actions = ["list", "add", "remove", "change", "quit"]
    catppuccin_mocha = {
        "rosewater": "#f5e0dc",
        "flamingo": "#f2cdcd",
        "pink": "#f5c2e7",
        "mauve": "#cba6f7",
        "red": "#f38ba8",
        "maroon": "#eba0ac",
        "peach": "#fab387",
        "yellow": "#f9e2af",
        "green": "#a6e3a1",
        "teal": "#94e2d5",
        "sky": "#89dceb",
        "sapphire": "#74c7ec",
        "blue": "#89b4fa",
        "lavender": "#b4befe",
        "text": "#cdd6f4",
        "subtext1": "#bac2de",
        "overlay2": "#9399b2",
        "surface2": "#585b70",
        "base": "#1e1e2e",
    }

    main_style = Style.from_dict({
        'qmark': f"fg:{catppuccin_mocha['mauve']} bold",
        'question': f"fg:{catppuccin_mocha['text']} bold",
        'answer': f"fg:{catppuccin_mocha['green']} bold",
        'pointer': f"fg:{catppuccin_mocha['blue']} bold",
        'highlighted': f"fg:{catppuccin_mocha['pink']} bold",
        'selected': f"fg:{catppuccin_mocha['peach']} bold",
        'separator': f"fg:{catppuccin_mocha['surface2']}",
        'instruction': f"fg:{catppuccin_mocha['overlay2']} italic",
        'text': f"fg:{catppuccin_mocha['text']}",
        'disabled': f"fg:{catppuccin_mocha['overlay2']} italic",
    })

    while True:
            if interactive:
                action = questionary.rawselect(
                    message="",
                    choices=[*actions],
                    qmark="> Select an action",
                    style=main_style).ask()
            else:
                action = questionary.text(message="> ", qmark="", style=main_style).ask()


            tasks = get_tasks()

            match action.lower():
                case "list":
                    list_tasks(tasks, nerd)

                case "add":
                     task = questionary.text(message = "Task name: ", qmark="", style=main_style).ask()
                     status = questionary.text(message = "Status name: ", qmark="", style=main_style).ask()
                     notes = questionary.text(message = "Notes name: ", qmark="", style=main_style).ask()

                     add_task(tasks, task, status, notes)

                case "change":
                    task_names = [tasks["tasks"][i]["name"] for i in range(len(tasks["tasks"]))]

                    to_change = questionary.rawselect(
                        "Select task to remove: ",
                        choices=[
                            *task_names
                        ],
                        style=main_style,
                        qmark="").ask()

                    idx = task_names.index(to_change) + 1

                    task = questionary.text(message = "Task name: ", qmark="", style=main_style).ask()
                    status = questionary.text(message = "Status name: ", qmark="", style=main_style).ask()
                    notes = questionary.text(message = "Notes name: ", qmark="", style=main_style).ask()

                    change_task(tasks, idx, task, status, notes)

                case "remove":
                    task_names = [tasks["tasks"][i]["name"] for i in range(len(tasks["tasks"]))]

                    to_change = questionary.rawselect(
                        "Select task to remove: ",
                        choices=[
                            *task_names
                        ],
                        style=main_style,
                        qmark="").ask()

                    idx = task_names.index(to_change) + 1

                    remove_task(tasks, idx)
                case "quit":
                    exit("Bye!")
                case _:
                    console.print("[red]An unknown error occurred.[/red]")
                    continue

if __name__ == "__main__":
    typer.run(main)