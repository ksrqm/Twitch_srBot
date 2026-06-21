import os
from dotenv import load_dotenv
from SR import playlist_randomizer

load_dotenv()
song_queue = []
songs_per_user = 1

def add_to_queue(song, ctx):
    streamer = os.getenv("TWITCH_CHANNEL")
    if ctx.author.name.lower() != streamer:
        user_songs = sum(
            1 for queued_song in song_queue
            if queued_song["user"].lower() == ctx.author.name.lower()
        )
        if user_songs >= songs_per_user:
            return False
    song_queue.append(song)
    print(
        f"Added: {song['title']}, duration: {song['duration']}, "
        f"user: {song['user']}, link: {song['link']}"
    )
    return True


def get_next_song():
    if song_queue:
        return song_queue.pop(0)
    elif playlist_randomizer.AUTO_PLAYLIST == "TRUE":
        return playlist_randomizer.get_random_song()
    return None

def get_queue():
    return song_queue.copy()