import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(ROOT_DIR, 'tasks.json')

CATPPUCCIN_MOCHA = {
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

QUESTIONARY_THEME = {
        'qmark': f"fg:{CATPPUCCIN_MOCHA['mauve']} bold",
        'question': f"fg:{CATPPUCCIN_MOCHA['text']} bold",
        'answer': f"fg:{CATPPUCCIN_MOCHA['green']} bold",
        'pointer': f"fg:{CATPPUCCIN_MOCHA['blue']} bold",
        'highlighted': f"fg:{CATPPUCCIN_MOCHA['pink']} bold",
        'selected': f"fg:{CATPPUCCIN_MOCHA['peach']} bold",
        'separator': f"fg:{CATPPUCCIN_MOCHA['surface2']}",
        'instruction': f"fg:{CATPPUCCIN_MOCHA['overlay2']} italic",
        'text': f"fg:{CATPPUCCIN_MOCHA['text']}",
        'disabled': f"fg:{CATPPUCCIN_MOCHA['overlay2']} italic",
    }
