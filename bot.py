import link_check
import os
import q
import player
from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()

bot = commands.Bot(
    token=os.getenv("TWITCH_TOKEN"),
    prefix="!",
    initial_channels=[os.getenv("TWITCH_CHANNEL")]
)


@bot.event()
async def event_ready():
    print(f"Bot is working. Reading chat in: {os.getenv('TWITCH_CHANNEL')}")
    await player.setup()

@bot.command()
async def song(ctx):
    song = await link_check.handle_song(ctx)
    if song:
        added = await q.filter_add_song(song, ctx)
        if added:
            await player.play(song, ctx)


if __name__ == "__main__":
    bot.run()