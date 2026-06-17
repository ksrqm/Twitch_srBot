from idlelib.debugobj_r import remote_object_tree_item

from twitchio import user

que = []
max_duration = 60*9

async def filter_add_song(song, ctx):
    print(song)
    if song["duration"]>=max_duration:
        print("ERROR: video max duration is up to 6 minutes")
        await ctx.send("video max duration is up to 6 minutes")
        return False
    else:
        que.append(song)
        print(f"Added: {song['title']}, duration: {song['duration']}, user: {song['user']}, link: {song['link']}")

        await ctx.send(f"Added: {song['title']}, duration: {song['duration']}, user: {song['user']}, link: {song['link']}")

        return True

def get_next_song():
    if len(que).pop(0):
        return None
    return que.pop(0)