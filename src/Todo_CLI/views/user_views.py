from rich.console import Console
from rich.style import Style
from rich.table import Table
from Todo_CLI.settings import CATPPUCCIN_MOCHA as C
from rich.box import ROUNDED
from rich.theme import Theme

CATPPUCCIN = Theme(C)

console = Console(theme=CATPPUCCIN)


# Resolve styles
text     = console.get_style("text")
subtext1 = console.get_style("subtext1")
surface2 = console.get_style("surface2")

# Header with a Catppuccin background band

title_style   = Style(color=C["mauve"], bold=True)
caption_style = Style(color=C["subtext1"], italic=True)

table = Table(
    box=ROUNDED,
    border_style=surface2,
    row_styles=[text, subtext1],  # zebra
    style=text,                   # default cell text
    title_style=title_style,
    caption_style=caption_style,
    show_lines=False,
    pad_edge=False,
)

table.title = "Tasks"
table.caption = "Be productive. Focus better."


table.add_column("Name")
table.add_column("Status")
table.add_column("Notes")

def render_tasks(tasks, nerd):
    if nerd:
        for idx, task in enumerate(tasks):
            if task.status == "Complete":
                table.add_row(f"{task.name}", "[green]󰄳 Completed[/green]",  f"{task.notes}")
            elif task.status == "In Progress":
                table.add_row(f"{task.name}", "[yellow]󰄯 In Progress[/yellow]",  f"{task.notes}")
            elif task.status == "Todo":
                table.add_row(f"{task.name}", "[bright_black]󰄰 Todo[/bright_black]",  f"{task.notes}")

    else:
        for idx, task in enumerate(tasks):
            if task.status == "Complete":
                table.add_row(f"{task.name}", "[green]◉ Completed[/green]",  f"{task.notes}")
            elif task.status == "In Progress":
                table.add_row(f"{task.name}", "[yellow]◐ In Progress[/yellow]", f"{task.notes}")
            elif task.status == "Todo":
                table.add_row(f"{task.name}", "[bright_black]◌ Todo[/bright_black]",  f"{task.notes}")

    console.print(table)
