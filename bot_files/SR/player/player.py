import asyncio

from bot_files.SR.player import player_local, player_youtube

from bot_files.SR import que

async def player_loop():
    while True:
        song = que.get_next_song()
        if song:
            if isinstance(song, dict):
                await player_youtube.play(song)
            else:
                await player_local.play_local(song)
        else:
            await asyncio.sleep(5)