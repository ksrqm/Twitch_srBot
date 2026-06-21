import os
import asyncio

from SR import player, link_check, playlist_randomizer, que

from dotenv import load_dotenv
from twitchio.ext import commands


load_dotenv()
bot = commands.Bot(
    token=str(os.getenv("TWITCH_TOKEN")),
    prefix="!",
    initial_channels=[os.getenv("TWITCH_CHANNEL")],
)
users_with_perms = str(os.getenv("USERS_WITH_PERMS")).split(',')

@bot.event()
async def event_ready():
    print(f"Bot is working. Reading chat in: {os.getenv('TWITCH_CHANNEL')}")
    playlist_randomizer.setup_local_playlist()
    asyncio.create_task(player.player_loop())

############################################################################
################################SONG REQUEST################################
############################################################################(
@bot.command()
async def song(ctx):
    request = await link_check.handle_song(ctx)
    if request:
        added = que.add_to_queue(request, ctx)
        await ctx.send(
            f"Added to queue: {request['title']} | "
            f"requested by {request['user']} | "
            f"{request['link']}")
        if not added:
            await ctx.send(f"Song limit per user exceeded")

@bot.command()
async def queue(ctx):
    songs = que.get_queue()
    if len(songs) == 0:
        await ctx.send("Queue is empty")
        return
    elif len(songs) > 3:
        text = " | ".join(song["title"] for song in songs[:3]) + f" | and {len(songs)-3} more"
        await ctx.send(f"Queue: {text}")
    else:
        text = " | ".join(song["title"] for song in songs[:3])
        await ctx.send(f"Queue: {text}")

@bot.command()
async def volume(ctx):
    if ctx.author.name.lower() == os.getenv('TWITCH_CHANNEL'):
        args = ctx.message.content.split()

        if len(args) < 2:
            await ctx.send("Usage: !volume <0-100>")
            return

        vol_arg = int(args[1])
        player.player.set_volume(vol_arg)
        await ctx.send(f"Volume set to {vol_arg}%")
    else:
        await ctx.send("Nice try rascal")

@bot.command()
async def skip(ctx):
    if ctx.author.name.lower() in users_with_perms:
        player.player.stop()
    else:
        await ctx.send("Nice try rascal")

@bot.command()
async def current(ctx):
    await ctx.send(f"Currently playing: {player.player.current_song}")

@bot.command()
async def pause(ctx):
    if ctx.author.name.lower() in users_with_perms:
        player.pause()
    else:
        await ctx.send("Nice try rascal")
############################################################################
############################################################################
############################################################################
if __name__ == "__main__":
    bot.run()