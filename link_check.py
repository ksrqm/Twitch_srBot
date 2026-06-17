import yt_dlp

async def handle_song(ctx):
    id = ctx.message.content.split(" ")[1]

    if len(id) == 11:
        link = "https://www.youtube.com/watch?v=" + id
        print("----------------------------------------------------------------")
        print(f"CHECKING LINK: {link}")

        try:
            with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
                info = ydl.extract_info(link, download=False)

            return {
                "title" : info.get("title"),
                "duration" : info.get("duration"),
                "link" : link,
                "user" : ctx.author.display_name
            }

        except Exception as e:
            print(f"Exception: {e}")
            await ctx.send(f"ID is not valid!")
            return False

    else:
        print("ID is not valid!")
        await ctx.send(f"ID is not valid!")
        return False