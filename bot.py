import link_check
import os
import q
import player
import asyncio
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
    asyncio.create_task(player.player_loop())

@bot.command()
async def song(ctx):
    player.ctx = ctx
    song = await link_check.handle_song(ctx)
    if song:
        await q.filter_add_song(song, ctx)

@bot.command()
async def skip(ctx):
    player.skip()

@bot.command()
async def queue(ctx):
    songs = q.get_queue()
    if len(songs) == 0:
        await ctx.send("Queue is empty")
        return
    text = " | ".join(song["title"] for song in songs[:3])
    await ctx.send(f"Queue: {text}")

if __name__ == "__main__":
    bot.run()