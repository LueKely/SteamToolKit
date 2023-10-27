# translate game description to whatever you fucking like you rat bastard
from googletrans import Translator
from ascii import list_languages
from rich.console import Console
from rich import print
from rich.prompt import Prompt


def translate_text(description):
  translator = Translator()
  console = Console()
  list_languages()
  
  dest = console.input("[magenta][bold]please insert you're preferable language using the language code: ")
  try:
    with console.status("[bold green]Fetching data...") as status:
      print("translating description")
      translated  = translator.translate(description,dest)
    console.log(f'[bold][red]Done!')
    print("[blue][bold]Your text: " + f"[green]{description}")
    print("[blue][bold]The translation in " + dest + ": " +f"[green]{translated.text}" )
  except Exception as e:
    console.log(f'[bold red]Error: {e}')
  
  choice = Prompt.ask("Translate it again? y/n", choices=["y", "n"], default="y")
  if(choice == 'y'):
    translate_text(description) 
  elif(choice =='n'):
    print("[bold][green]Will do!")

# translate_text("testing")