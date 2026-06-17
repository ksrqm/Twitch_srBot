import link_check
import os
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


@bot.command()
async def song(ctx):
    await link_check.handle_song(ctx)


if __name__ == "__main__":
    bot.run()