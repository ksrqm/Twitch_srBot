import os
import random

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

osu_state=os.getenv('OSU_STATE')
AUTO_PLAYLIST=os.getenv("AUTO_PLAYLIST")

local_playlist = []


def setup_local_playlist():
    global local_playlist

    if AUTO_PLAYLIST == "FALSE":
        return

    if osu_state == "TRUE":
        return

    path = Path(os.getenv("PLAYLIST_PATH"))

    local_playlist = [
        file
        for file in path.iterdir()
        if file.is_file()
        and file.suffix.lower() == ".mp3"
    ]

    print(f"Loaded {len(local_playlist)} songs")


def get_random_song():
    if osu_state == "TRUE":
        return get_osu_song()
    return random.choice(local_playlist)


def get_osu_song():
    path = Path(os.getenv("PLAYLIST_PATH_OSU"))
    folders = [
        folder
        for folder in path.iterdir()
        if folder.is_dir()
    ]
    while True:
        folder = random.choice(folders)

        mp3_files = [
            file
            for file in folder.iterdir()
            if file.is_file()
            and file.suffix.lower() == ".mp3"
        ]

        if mp3_files:
            return random.choice(mp3_files)