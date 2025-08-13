from pathlib import Path
import customtkinter

default_theme_path = Path(__file__).parent.parent / "assets" / "themes" / "default.json"

def set_default_theme():
    customtkinter.set_default_color_theme(default_theme_path)