# STEAM TOOLKIT: A TERMINAL COMMAND LINE PROGRAM

## AUTHOR: Anunciacion Lue Kely D.

## WHAT IS IT?:

- steam toolkit allows the user to access the steam web api using the `python-steam-api 1.2.0`
  which can do the following:
  - allow users to see public steam profiles via steam ID or steam name
  - access game data using the game's steam ID or the name of the game
  - get the list of friends of steam user with their steam ID

## WHAT IS INTIGRATED?

Google translate: - you can translate game descriptions with the `googletrans` api when using the `game details` command
example command: - type `game details` - and enter the steam id of the game eg: `105600` - and choose the language of your choosing - if you don't know what the steam id of the game you'd like to see, you can always use the `search game` command
to see what the steam id of the game

QR Code: - when getting the info of a user using the `search user` there is an option to save the user's profile picture as a qr code
use the `qrcode` api.

## IF YOU DON'T HAVE ANY STEAM ID'S you know or have:

you can use these ones
steam id for users:

- 76561198995017863
- 76561198334890736
- 76561198867251184

steam id for games:

- 105600
- 2344520

## Setup

### setting up the environment

in the terminal type:
`python -m venv myenv`
`myenv\Scripts\activate`

### setting up the independencies

    in the terminal type:
      `pip install -r requirements.txt`
