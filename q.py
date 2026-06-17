que = []
max_duration = 60 * 9

async def filter_add_song(song, ctx):
    print(song)
    if song["duration"] >= max_duration:
        print("ERROR: video max duration is up to 9 minutes")
        await ctx.send("Video max duration is up to 9 minutes")
        return False
    que.append(song)
    print(
        f"Added: {song['title']}, duration: {song['duration']}, "
        f"user: {song['user']}, link: {song['link']}"
    )
    await ctx.send(
        f"Added: {song['title']}, user: {song['user']}"
        f"link: {song['link']}"
    )
    return True

def get_next_song():
    if len(que) == 0:
        return None
    return que.pop(0)

def get_queue():
    return que