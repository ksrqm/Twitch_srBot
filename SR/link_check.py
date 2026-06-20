import yt_dlp

async def handle_song(ctx):
    args = ctx.message.content.split()
    if len(args) < 2:
        await ctx.send("You need to provide YouTube ID")
        return False
    song_id = args[1]

    if len(song_id) == 11:
        link = "https://www.youtube.com/watch?v=" + song_id
        print("----------------------------------------------------------------")
        print(f"CHECKING LINK: {link}")

        try:
            with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
                info = ydl.extract_info(link, download=False)

            song_info={
                "title": info.get("title"),
                "duration": info.get("duration"),
                "link": link,
                "user": ctx.author.display_name
            }

            message = filter_song(song_info)

            if message:
                await ctx.send(message)
                return False
            return song_info

        except Exception as e:
            print(f"Exception: {e}")
            await ctx.send(f"Something went wrong. {e}")
            return False
    else:
        print("ID is not valid!")
        await ctx.send(f"ID is not valid!")
        return False



def filter_song(song_info):
    words = ["nigga", "nigger", "niggas", "niggers"]

    if song_info["duration"] and song_info["duration"] > 480:
        print("Song too long")
        return f"Song longer than 8 minutes | {song_info['title']}"

    for word in words:
        if word in song_info["title"].lower():
            print("Song filtered")
            return "Song filtered"

    return None