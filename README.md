# Installation

## Requirements

* Windows
* VLC Media Player installed
* Python

## Quick Install
1. Install Python
 
https://www.python.org/

2. Install VLC Media Player

https://www.videolan.org/

3. Install the bot

Open Command Prompt in the project directory and run:

`python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt`

4. Configure the bot

Rename .env.example to .env and fill in the required values.

5. Run the bot

Start the bot using: start.bat
## Configuration

Rename `.env.example` to `.env` and fill in:

* `TWITCH_TOKEN`
* `TWITCH_CHANNEL`

and settings:

bot checks only for TRUE so if you put "Mona Lisa" for example it'll still work
* `AUTO_PLAYLIST=TRUE`
* `OSU_STATE=TRUE`
* `PLAYLIST_PATH_OSU=...`
* `PLAYLIST_PATH=...`
* `USERS_WITH_PERMS=...`

## Commands
* `!song <youtube_id>` - add song request
* `!skip` - skip current song
* `!volume <0-100>` - set volume
* `!queue` - show queue
* `!current` - show currently playing song
* `!pause` - pause currently playing song

# Note
in case of problems or questions you can reach me on discord

ksrqm aka Vanitas

![img.png](img.png)
