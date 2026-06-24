import asyncio
from bot_files.SR import playlist_randomizer
from bot_files.SR.bot_setup import bot, channel
from bot_files.SR.player import player
from bot_files.logger import log_returns


@bot.event()
async def event_ready():
    log_returns.log_event_ready(channel)
    playlist_randomizer.setup_local_playlist()
    asyncio.create_task(player.player_loop())