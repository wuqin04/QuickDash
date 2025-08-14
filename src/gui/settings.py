from pathlib import Path
import customtkinter

APP_TITLE = "QuickDash"
APP_SIZE = "680x400"

default_theme_path = Path(__file__).parent.parent / "assets" / "themes" / "default.json"

def set_default_appearance_mode():
    customtkinter.set_appearance_mode("system")

def set_default_theme():
    customtkinter.set_default_color_theme(default_theme_path)