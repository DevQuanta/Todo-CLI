from rich.console import Console

console = Console()


def render_tasks(tasks, nerd):
    if nerd:
        for idx, task in enumerate(tasks):
            if task.status == "Complete":
                task_fmt = f"""[green]󰄳 {task.name}\n  {task.notes}[/green]"""

                console.print(task_fmt)
            elif task.status == "In Progress":
                task_fmt = f"""[yellow]󰄯 {task.name}\n  {task.notes}[/yellow]"""

                console.print(task_fmt)
            elif task.status == "Todo":
                task_fmt = f"""[bright_black]󰄰 {task.name}\n  {task.notes}[/bright_black]"""

                console.print(task_fmt)
    else:
        for idx, task in enumerate(tasks):
            if task.status == "Complete":
                task_fmt = f"""[green]◉ {task.name}\n  {task.notes}[/green]"""

                console.print(task_fmt)
            elif task.status == "In Progress":
                task_fmt = f"""[yellow]◐ {task.name}\n  {task.notes}[/yellow]"""

                console.print(task_fmt)
            elif task.status == "Todo":
                task_fmt = f"""[bright_black]◌ {task.name}\n  {task.notes}[/bright_black]"""

                console.print(task_fmt)
