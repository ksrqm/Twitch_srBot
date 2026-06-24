import yt_dlp
import asyncio
import vlc

from bot_files.SR.player import player_setup

from bot_files.logger import log_returns


def get_audio_url(link):
    options = {
        "format": "bestaudio",
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(link, download=False)

    return info["url"]

async def play(song):
    audio_url = get_audio_url(song["link"])
    log_returns.log_play_youtube(song["link"], song["title"])
    player_setup.player.play_media(audio_url)
    player_setup.player.current_song = song["link"]

    await asyncio.sleep(3)
    while True:
        if player_setup.player.skip:
            break
        state = player_setup.player.vlc_player.get_state()
        if state == vlc.State.Ended:
            break
        if state == vlc.State.Error:
            break
        await asyncio.sleep(1)