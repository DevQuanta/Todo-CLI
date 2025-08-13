import json
from rich.console import Console
import typer
from typing_extensions import Annotated
import questionary
from questionary import Style


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
    main_style = Style([
        ('qmark', 'fg:#673ab7 bold'),  # token in front of the question
        ('question', 'bold'),  # question text
        ('answer', 'fg:#f44336 bold'),  # submitted answer text behind the question
        ('pointer', 'fg:#673ab7 bold'),  # pointer used in select and checkbox prompts
        ('highlighted', 'fg:#673ab7 bold'),  # pointed-at choice in select and checkbox prompts
        ('selected', 'fg:#cc5454'),  # style for a selected item of a checkbox
        ('separator', 'fg:#cc5454'),  # separator in lists
        ('instruction', ''),  # user instructions for select, rawselect, checkbox
        ('text', ''),  # plain text
        ('disabled', 'fg:#858585 italic')  # disabled choices for select and checkbox prompts
    ])

    while True:
        # action = input("add, list, change, or remove tasks: ")

        if interactive:
            action = questionary.select(
                message="",
                choices=[*actions],
                instruction=" ",
                qmark="> ",
                style=main_style).ask()
        else:
            action = questionary.text(message="> ", qmark="", style=main_style).ask()


        tasks = get_tasks()

        match action.lower():
            case "list":
                list_tasks(tasks, nerd)

            case "add":
                task = input("Task name: ")
                status = input("Status: ")
                notes = input("Notes: ")
                add_task(tasks, task, status, notes)

            case "change":
                idx = int(input("Enter task number to change: ")) - 1

                task = input("Task name: ")
                status = input("Status: ")
                notes = input("Notes: ")

                change_task(tasks, idx, task, status, notes)

            case "remove":
                idx = int(input("Enter task number to remove: ")) - 1

                remove_task(tasks, idx)
            case "quit":
                exit("Bye!")
            case _:
                print("Please enter a valid command.")
                continue


if __name__ == "__main__":
    typer.run(main)
