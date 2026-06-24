import vlc


class Player:
    def __init__(self):
        self.vlc_player = vlc.MediaPlayer()
        self.vlc_player.audio_set_volume(20)
        self.skip = False
        self.current_song = None

    def set_volume(self, volume):
        self.vlc_player.audio_set_volume(volume)

    def skip_song(self):
        self.skip = True
        self.vlc_player.stop()

    def pause(self):
        self.vlc_player.pause()

    def play_media(self, path):
        self.skip = False

        media = vlc.Media(str(path))
        self.vlc_player.set_media(media)
        self.vlc_player.play()

    def is_playing(self):
        return self.vlc_player.is_playing()


player = Player()