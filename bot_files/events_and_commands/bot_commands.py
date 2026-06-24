from bot_files.SR import link_check, que
from bot_files.SR.bot_setup import bot, channel, users_with_perms
from bot_files.SR.player import player_setup
from bot_files.logger import log_returns
from logger.log_returns import log_answer


############################################################################
################################ FOR STREAMER ##############################
############################################################################
@bot.command()
async def volume(ctx):
    if ctx.author.name.lower() == channel:
        args = ctx.message.content.split()

        if len(args) < 2:
            return

        vol_arg = int(args[1])
        player_setup.player.set_volume(vol_arg)
        log_returns.log_volume(False, vol_arg, ctx.author.name)
    else:
        await ctx.send("Nice try rascal")
        log_returns.log_volume(False, None, ctx.author.name)
############################################################################
################################ FOR MODS ##################################
############################################################################
@bot.command()
async def pause(ctx):
    if ctx.author.name.lower() in users_with_perms:
        player_setup.player.pause()
        log_returns.log_pause(False, player_setup.player.is_playing(), ctx.author.name)
    else:
        await ctx.send("Nice try rascal")
        log_returns.log_pause(True, player_setup.player.is_playing(), ctx.author.name)


@bot.command()
async def skip(ctx):
    if ctx.author.name.lower() in users_with_perms:
        player_setup.player.skip_song()
        log_returns.log_skip(False, ctx.author.name)
    else:
        await ctx.send("Nice try rascal")
        log_returns.log_skip(True, ctx.author.name)
############################################################################
############################# FOR EVERYONE #################################
############################################################################
@bot.command()
async def song(ctx):
    try:
        request = await link_check.handle_song(ctx)
    except ValueError:
        answer = "Invalid link"
        await ctx.send(answer)
        log_answer(answer)
        return

    if request:
        added = que.add_to_queue(request, ctx)
        log_returns.log_song(request['title'], request['user'], request['link'])

        answer = (
            f"Added to queue: {request['title']} | "
            f"requested by {request['user']} | "
            f"{request['link']}")
        await ctx.send(answer)
        log_answer(answer)

        if not added:
            await ctx.send(f"Song limit per user exceeded")


@bot.command()
async def queue(ctx):
    log_returns.log_queue(ctx.author.name)
    songs = que.get_queue()

    if len(songs) == 0:
        answer = "Queue is empty"
        await ctx.send(answer)
        log_answer(answer)
        return
    elif len(songs) > 3:
        text = " | ".join(song["title"] for song in songs[:3]) + f" | and {len(songs)-3} more"
        answer = f"Queue: {text}"
        await ctx.send(answer)
        log_answer(answer)
    else:
        text = " | ".join(song["title"] for song in songs[:3])
        answer = f"Queue: {text}"
        await ctx.send(answer)
        log_answer(answer)


@bot.command()
async def current(ctx):
    answer = f"Currently playing: {player_setup.player.current_song}"
    log_returns.log_current(ctx.author.name)
    await ctx.send(answer)
    log_answer(answer)