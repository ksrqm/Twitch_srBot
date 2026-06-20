from SR import playlist_randomizer

song_queue = []

def add_to_queue(song):
    song_queue.append(song)

    print(
        f"Added: {song['title']}, duration: {song['duration']}, "
        f"user: {song['user']}, link: {song['link']}"
    )


def get_next_song():
    if song_queue:
        return song_queue.pop(0)
    elif playlist_randomizer.AUTO_PLAYLIST == "TRUE":
        return playlist_randomizer.get_random_song()
    return None

def get_queue():
    return song_queue.copy()