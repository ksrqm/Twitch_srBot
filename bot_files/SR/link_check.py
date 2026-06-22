import yt_dlp
from urllib.parse import urlparse, parse_qs

supported_hostnames = {
        "www.youtube.com",
        "youtube.com",
        "youtu.be",
        "music.youtube.com"
    }

async def handle_song(ctx):
    args = ctx.message.content.split(" ")
    #validate_link(args[1], args, ctx)
    link = clean_link(args[1])

    if not link.startswith(("http://", "https://")):
        link = "https://" + link

    print("----------------------------------------------------------------")
    print(f"CHECKING LINK: {link}")

    hostname = urlparse(link).hostname

    try:
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
        return False

def validate_link(link, args, ctx):
    print("_______")
    parsed = urlparse(link)
    print("_______")

    if len(args) < 2:
        print(f"----------------------------------------------------------------\n{link}\nInvalid link")
        raise ValueError

    if not parsed.hostname in supported_hostnames or not parsed.hostname:
        print(f"----------------------------------------------------------------\n{link}\nInvalid link")
        raise ValueError



def clean_link(link: str):
    parsed = urlparse(link)

    if parsed.hostname == "youtu.be":
        return link.split("?")[0]
    if "youtube.com" in parsed.hostname:
        video_id = parse_qs(parsed.query).get("v")
        if video_id:
            print(f"https://www.youtube.com/watch?v={video_id[0]}")
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