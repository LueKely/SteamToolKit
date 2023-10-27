from rich import print
from ascii import ascii_title, column, list_commands
from rich.prompt import Prompt
import commands

def command_prompt():
    name = Prompt.ask("Enter your command")
    match name:
        case "help":
            commands.list_commands()
            command_prompt()
        case "exit":
            print("exiting...")
        case "search game":
            input = Prompt.ask("Enter the name of the game")
            commands.search_game_name(input)
            command_prompt()
        case "game details":
            input = Prompt.ask("Enter the id of the game")
            commands.search_game_details(input)
            command_prompt()
        case "search user":
            choice = Prompt.ask("Search By Id or by name", choices=["id", "name"], default="id")
            match choice:
                case "id":
                    id = Prompt.ask("Enter the user id")
                    commands.search_user_id(id)
                    command_prompt()
                case "name":
                    name = Prompt.ask("Enter the user name")
                    commands.search_user_name(name)
                    command_prompt()
        case "list friends":
            id = Prompt.ask("Enter the user id")
            commands.list_friends(id)
            command_prompt()
        case _:
            print("invalid command")
            command_prompt()

def title():
    column()
    ascii_title()
    column()
    list_commands()
    command_prompt()

def main():
    title()



main()
