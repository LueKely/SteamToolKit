from rich.console import Console
from rich.table import Table
from googletrans import LANGUAGES
from rich.prompt import Prompt


def ascii_title():
    print(" ____ _____ _____    _    __  __   _____ ___   ___  _  __  _  _____ _____ ")
    print("/ ___|_   _| ____|  / \  |  \/  | |_   _/ _ \ / _ \| |/ / | |/ |_ _|_   _|")
    print("\___ \ | | |  _|   / _ \ | |\/| |   | || | | | | | | ' /  | ' / | |  | |  ")
    print(" ___) || | | |___ / ___ \| |  | |   | || |_| | |_| | . \  | . \ | |  | |  ")
    print("|____/ |_| |_____/_/   \_|_|  |_|   |_| \___/ \___/|_|\_\ |_|\_|___| |_|  ")


def column():
    print("===========================================================================================================================")


def list_commands():
    console = Console()
    table = Table(title="Commands")
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta", no_wrap=True)
    table.add_row("help", "Lists all commands")
    table.add_row("list friends", "displays user's friends steam id")
    table.add_row(
        "search user", "searches for a user by steam id or steam name")
    table.add_row(
        "search game", "searches for a game by steam name")
    table.add_row(
        "game details", "searches for a game by steam id")
    table.add_row(
        "exit", "close program")
    console.print(table)


def list_languages():
    console = Console()
    table = Table(title="Languages")
    table.add_column("Language", style="cyan", no_wrap=True)
    table.add_column("Language Code", style="magenta", no_wrap=True)
    for key, value in LANGUAGES.items():
        table.add_row(value, key)
    console.print(table)
