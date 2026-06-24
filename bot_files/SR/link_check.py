import yt_dlp

from urllib.parse import urlparse, parse_qs

from bot_files.logger import log_returns


supported_hostnames = {
        "www.youtube.com",
        "youtube.com",
        "youtu.be",
        "music.youtube.com"
    }

async def handle_song(ctx):
    args = ctx.message.content.split(" ")
    validate_link(args)
    link = clean_link(args[1])

    if not link.startswith(("http://", "https://")):
        link = "https://" + link

    print("________________________________________________________________________________")
    log_returns.log_answer(
        f"CHECKING LINK: {link}"
    )

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
        answer = filter_song(song_info)

        if answer:
            await ctx.send(answer)
            log_returns.log_answer(answer)
            return False

        return song_info

    except Exception as e:
        return False

def validate_link(args):
    if len(args) < 2:
        print(f"________________________________________________________________________________\nInvalid link")
        raise ValueError

    parsed = urlparse(args[1])

    if not parsed.hostname in supported_hostnames or not parsed.hostname:
        print(f"________________________________________________________________________________\nInvalid link")
        raise ValueError



def clean_link(link: str):
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

    if song_info["duration"] and song_info["duration"] > 480 or song_info["duration"] is None:
        print("Song too long")
        return f"Song longer than 8 minutes | {song_info['title']}"

    for word in words:
        if word in song_info["title"].lower():
            print("Song filtered")
            return "Song filtered"

    return None