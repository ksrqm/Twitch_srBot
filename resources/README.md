# Installation

## Requirements

### Running the executable
* VLC Media Player installed

### Running from source
* VLC Media Player installed
* Python 3.10+

# Quick Install

1. Install VLC Media Player

https://www.videolan.org/

2. Download the latest release

3. Configure the bot

Rename `.env.example` to `.env` and fill in the required values (instructions in the file and below)

4. Run the .exe file

## Configuration

Rename `.env.example` to `.env` and fill in:

* `TWITCH_TOKEN`
* `TWITCH_CHANNEL`

and settings:

bot checks only for "TRUE" value so if you put "Mona Lisa" for example it'll still work
* `AUTO_PLAYLIST=TRUE`
* `OSU_STATE=TRUE`
* `PLAYLIST_PATH_OSU=...`
* `PLAYLIST_PATH=...`
* `USERS_WITH_PERMS=...`

## Commands
* `!song <youtube link>` - add song request
* `!skip` - skip current song
* `!volume <0-100>` - set volume
* `!queue` - show queue
* `!current` - show currently playing song
* `!pause` - pause currently playing song

# Note
in case of problems or questions you can reach me on discord

ksrqm aka Vanitas

![img.png](img.png)
