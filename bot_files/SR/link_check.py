import yt_dlp
from urllib.parse import urlparse, parse_qs

async def handle_song(ctx):
    args = ctx.message.content.split(" ")

    if len(args) < 2:
        await ctx.send("You need to provide YouTube link")
        return False

    link = clean_link(args[1])

    if not link.startswith(("http://", "https://")):
        link = "https://" + link

    print("----------------------------------------------------------------")
    print(f"CHECKING LINK: {link}")

    hostname = urlparse(link).hostname

    if not hostname or not (
        hostname == "youtu.be"
        or hostname == "youtube.com"
        or hostname.endswith(".youtube.com")
    ):
        print("Link is not valid!")
        await ctx.send("Link is not valid!")
        return False

    try:
        print("starting dlp")
        with yt_dlp.YoutubeDL({
            "quiet": True,
            "no_warnings": True
        }) as ydl:
            info = ydl.extract_info(link, download=False)

        song_info = {
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

def clean_link(link):
    parsed = urlparse(link)
    if parsed.hostname == "youtu.be":
        return link.split("?")[0]
    if "youtube.com" in parsed.hostname:
        video_id = parse_qs(parsed.query).get("v")

        if video_id:
            return f"https://www.youtube.com/watch?v={video_id[0]}"
    return link

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