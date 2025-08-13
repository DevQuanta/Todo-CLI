import os
from rich.console import Console
import questionary

console = Console()

class SetupWizard:
    def __init__(self, config_path):
        self.config_file = os.path.join(config_path, 'config.yaml')

    def setup(self):
        config = questionary.path(message=f"Config location (default: {self.config_file})").ask()

        console.print("[/yellow]Configuring Taskit...[/yellow]")


