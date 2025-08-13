from rich.console import Console
import typer
from typing_extensions import Annotated
import questionary
from prompt_toolkit.styles import Style

from Todo_CLI.settings import FILE_PATH, QUESTIONARY_THEME
from Todo_CLI.services.task_service import TaskService
from Todo_CLI.storage.local import LocalStorage
from Todo_CLI.views.user_views import render_tasks

console = Console()


def main(nerd: Annotated[bool, typer.Option(help="Use nerd font glyphs")] = False,
         interactive: Annotated[bool, typer.Option(help="Use interactive mode for CLI")] = False):
    actions = ["list", "add", "remove", "change", "quit"]

    main_style = Style.from_dict(QUESTIONARY_THEME)
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
