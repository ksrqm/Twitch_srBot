import vlc
import asyncio
import yt_dlp
import os
import re

from pathlib import Path
from SR import que


class Player:
    def __init__(self):
        self.vlc_player = vlc.MediaPlayer()
        self.vlc_player.audio_set_volume(20)
        self.skip = False
        self.current_song = None

    def set_volume(self, volume):
        self.vlc_player.audio_set_volume(volume)

    def stop(self):
        self.skip = True
        self.vlc_player.stop()

    def play_media(self, path):
        self.skip = False

        media = vlc.Media(str(path))
        self.vlc_player.set_media(media)
        self.vlc_player.play()

    def is_playing(self):
        return self.vlc_player.is_playing()


player = Player()

def pause():
    player.vlc_player.pause()

async def play(song):
    audio_url = get_audio_url(song["link"])
    player.play_media(audio_url)
    player.current_song = song["link"]
    await asyncio.sleep(3)
    while True:
        if player.skip:
            break
        state = player.vlc_player.get_state()
        if state == vlc.State.Ended:
            break
        if state == vlc.State.Error:
            break
        await asyncio.sleep(1)

async def play_local(path):
    if os.getenv("OSU_STATE") == "TRUE":
        name = Path(path).parent.name
        name = re.sub(r"^\d+\s*", "", name)
    else:
        name = Path(path).stem
    player.current_song = name
    print(f"Playing local: {path}")
    player.play_media(path)
    await asyncio.sleep(1)
    while True:
        if player.skip:
            break
        state = player.vlc_player.get_state()
        if state == vlc.State.Ended:
            break
        if state == vlc.State.Error:
            break
        await asyncio.sleep(1)


def get_audio_url(link):
    options = {
        "format": "bestaudio",
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(link, download=False)

    return info["url"]


async def player_loop():
    while True:
        song = que.get_next_song()
        if song:
            if isinstance(song, dict):
                await play(song)
            else:
                await play_local(song)
        else:
            await asyncio.sleep(5)