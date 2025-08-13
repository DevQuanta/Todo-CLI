import json
from rich.console import Console
import typer
from typing_extensions import Annotated
import questionary
from prompt_toolkit.styles import Style
from services.task_service import TaskService
from storage.local import LocalStorage
from views.user_views import render_tasks
from settings import FILE_PATH

console = Console()


def get_tasks(tasks):
    with open("tasks.json", "r") as file:
        task_json = json.load(file)

    for idx in range(len(task_json["tasks"])):
        task_name = task_json["tasks"][idx]["name"]
        task_status = task_json["tasks"][idx]["status"]
        task_notes = task_json["tasks"][idx]["notes"]

        new_task = task.Task(task_name, task_status, task_notes)
        tasks.add_task(new_task)

    return tasks


# def list_tasks(tasks, nerd):
#
#     if nerd:
#         for idx, task in enumerate(tasks):
#             if task.status == "Complete":
#                 task_fmt = f"""[green]󰄳 {task.name}\n  {task.notes}[/green]"""
#
#                 console.print(task_fmt)
#             elif task.status == "in progress":
#                 task_fmt = f"""[yellow]󰄯 {task.name}\n  {task.notes}[/yellow]"""
#
#                 console.print(task_fmt)
#             elif task.status == "todo":
#                 task_fmt = f"""[bright_black]󰄰 {task.name}\n  {task.notes}[/bright_black]"""
#
#                 console.print(task_fmt)
#     else:
#         for idx, task in enumerate(tasks):
#             if task.status == "complete":
#                 task_fmt = f"""[green]◉ {task.name}\n  {task["notes"]}[/green]"""
#
#                 console.print(task_fmt)
#             elif task.status == "in progress":
#                 task_fmt = f"""[yellow]◐ {task.name}\n  {task.notes}[/yellow]"""
#
#                 console.print(task_fmt)
#             elif task.status == "todo":
#                 task_fmt = f"""[bright_black]◌ {task.name}\n  {task.notes}[/bright_black]"""
#
#                 console.print(task_fmt)

def main(nerd: Annotated[bool, typer.Option(help="Use nerd font glyphs")] = False,
         interactive: Annotated[bool, typer.Option(help="Use interactive mode for CLI")] = False):
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
                qmark="> select an action",
                style=main_style).ask()
        else:
            action = questionary.text(message="> ", qmark="", style=main_style).ask()

        local = LocalStorage(FILE_PATH)
        tasks = TaskService(storage=local)

        task_list = tasks.list_tasks()

        match action.lower():
            case "list":
                render_tasks(task_list, nerd)

            case "add":
                name = questionary.text(message="Task name: ", qmark="", style=main_style).ask()
                status = questionary.text(message="Status: ", qmark="", style=main_style).ask()
                notes = questionary.text(message="Notes: ", qmark="", style=main_style).ask()

                tasks.add_task(name, status, notes)
                tasks.commit()

            case "change":
                task_names = [task_list[i].name for i in range(len(task_list))]

                to_change = questionary.rawselect(
                    "Select task to remove: ",
                    choices=[
                        *task_names
                    ],
                    style=main_style,
                    qmark="").ask()

                idx = task_names.index(to_change)

                name = questionary.text(message="Task name: ", qmark="", style=main_style).ask()
                status = questionary.text(message="Status name: ", qmark="", style=main_style).ask()
                notes = questionary.text(message="Notes name: ", qmark="", style=main_style).ask()

                tasks.change_task(idx, name, status, notes)
                tasks.commit()

            case "remove":
                task_names = [task_list[i].name for i in range(len(task_list))]

                to_change = questionary.rawselect(
                    "Select task to remove: ",
                    choices=[
                        *task_names
                    ],
                    style=main_style,
                    qmark="").ask()

                idx = task_names.index(to_change)

                tasks.remove_task(idx)
                tasks.commit()

            case "quit":
                exit("Bye!")
            case _:
                console.print("[red]An unknown error occurred.[/red]")
                continue


if __name__ == "__main__":
    typer.run(main)
