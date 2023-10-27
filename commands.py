# commands:
# help done
# news
# search user done
# search game
# list friends done
# list sales

from ascii import list_commands
from steam import Steam
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print
from translate import translate_text
from rich.prompt import Prompt
from generateQR import generateQR

# globals
console = Console()
steam = Steam("4FC14CDA81277425EB31813BD82E74E2")

def help():
    list_commands()

# natamad na ko di ko na iibahin tung dalawa lol
def search_user_id(user):

        try:
            with console.status("[bold green]Fetching data...") as status: 
                user = steam.users.get_user_details(user)
                print("[green][bold]Information about user:")

            # create za table
                table = Table(title="Results")
                table.add_column("key", style="cyan", no_wrap=True)
                table.add_column("value", style="magenta", no_wrap=True)
                for key, value in user["player"].items():
                    table.add_row(f"{key}", f"{value}")
                console.print(table)

        except:
     
            print("User not found.")
        
        choice = Prompt.ask("[bold][yellow]Would you like to save player avatar as qr code?", choices=["y", "n"], default="y")
        if choice == 'y':
            generateQR(user["player"]["avatarfull"])
            print("[bold][green]QR code saved as qr.png")
       


def search_user_name(user):
    try:
        # create za table
        with console.status("[bold green]Fetching data...") as status: 
            user = steam.users.search_user(user)
            table = Table(title="Results")
            table.add_column("key", style="cyan", no_wrap=True)
            table.add_column("value", style="magenta", no_wrap=True)
            for key, value in user["player"].items():
                table.add_row(f"{key}", f"{value}")
            console.print(table)

    except:
        print("User not found.")
    
    choice = Prompt.ask("[bold][yellow]Would you like to save player avatar as qr code?", choices=["y", "n"], default="y")
    if choice == 'y':
        generateQR(user["player"]["avatarfull"])
        print("[bold][green]QR code saved as qr.png please check the directory of the program")
       


def list_friends(id):
    try:
        with console.status("[bold green]Fetching data...") as status:
            user = steam.users.get_user_friends_list(id)
            output = ""
            for friends in user['friends']:
                output += f"{friends['steamid']}\n"
        
        print(Panel(output, title="List of friend's steam id",
              subtitle=f"currrent friends:{len(user['friends'])}"))
    except:
        print("[red][bold]error something went wrong")


def search_game_name(gameName):
    try:
        with console.status("[bold green]Fetching data...") as status:
            games = steam.apps.search_games(gameName)
        
            table = Table(title="Results")
            table.add_column("id", style="cyan")
            table.add_column("link", style="cyan")
            table.add_column("name", style="cyan")
            table.add_column("img", style="cyan")
            table.add_column("price", style="cyan")
            for game in games['apps']:
                table.add_row(f"{game['id']}", f"{game['link']}",f"{game['name']}", f"{game['img']}", f"{game['price']}")
            console.print(table)
    except:
        print("[red][bold]error something went wrong")




def search_game_details(id):
    try:
        with console.status("[bold green]Fetching data...") as status:
            user = steam.apps.get_app_details(id)

        if (user[id]["success"] == False):
            print("game not found")
            return None

        table = Table(title="Results")
        table.add_column("type", style="cyan")
        table.add_column("name", style="cyan")
        table.add_column("steam_appid", style="cyan")
        table.add_column("required_age", style="cyan")
        table.add_column("short_description", style="cyan")

        table.add_row(f"{user[id]['data']['type']}", f"{user[id]['data']['name']}", f"{user[id]['data']['steam_appid']}",
                      f"{user[id]['data']['required_age']}", f"{user[id]['data']['short_description']}")
        console.print(table)
        choice = Prompt.ask("Translate it? y/n", choices=["y", "n"], default="y")
        if(choice == 'y'):
            translate_text(user[id]['data']['short_description'])
        elif(choice =='n'):
            print("[bold][green]Will do!")
    except:
        print("[red][bold]error something went wrong")
        



