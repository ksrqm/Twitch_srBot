import os
import re
import asyncio
import vlc

from pathlib import Path

from bot_files.SR.player import player_setup

from bot_files.logger import log_returns


async def play_local(path):
    if os.getenv("OSU_STATE") == "TRUE":
        name = Path(path).parent.name
        name = re.sub(r"^\d+\s*", "", name)
    else:
        name = Path(path).stem
    player_setup.player.current_song = name

    log_returns.log_play_local(path)
    player_setup.player.play_media(path)

    await asyncio.sleep(1)
    while True:
        if player_setup.player.skip:
            break
        state = player_setup.player.vlc_player.get_state()
        if state == vlc.State.Ended:
            break
        if state == vlc.State.Error:
            break
        await asyncio.sleep(1)