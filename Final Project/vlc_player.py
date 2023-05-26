import pafy
import vlc


class VlcPlayer:
    """This class is responsible for creating a Vlc Player and loading the proper YouTube video into the player."""
    def __init__(self):
        self.instance = None
        self.player = None
        self.media = None

    def create_instance(self, window_id, url):
        """Creates a vlc and player instance so videos can be viewed locally via a tkinter window"""
        if self.instance is None or self.player is None:
            self.instance = vlc.Instance()
            self.player = self.instance.media_player_new()
            self.player.set_hwnd(window_id)
        self.stop()
        self._load_video(url)

    def _load_video(self, url):
        """Private method to VlcPlayer class that is responsible for loading a YouTube video stream through pafy"""
        if self.instance is None or self.player is None:
            raise RuntimeError('Must create instance before loading video')
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        self.media = self.instance.media_new(playurl)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.video_set_scale(0)

    def play(self):
        """Play VLC Video, requires proper player and creation"""
        if self.player is not None:
            self.player.play()

    def pause(self):
        """Pause VLC Video, requires proper player and creation"""
        if self.player is not None:
            self.player.set_pause(1)

    def stop(self):
        """Stop VLC Video, requires proper player and creation"""
        if self.player is not None:
            self.player.stop()

    def rewind(self, scale):
        """Rewind VLC Video, requires proper player and creation"""
        if self.player is not None:
            self.player.set_position(self.player.get_position() - scale)

    def fast(self, scale):
        """Fast Forward VLC Video, requires proper player and creation"""
        if self.player is not None:
            self.player.set_position(self.player.get_position() + scale)

    def volume_down(self, scale):
        """Change Volume Down, requires proper player and creation"""
        if self.player is not None:
            volume = self.player.audio_get_volume()
            self.player.audio_set_volume(volume - scale)

    def volume_up(self, scale):
        """Change Volume Up, requires proper player and creation"""
        if self.player is not None:
            volume = self.player.audio_get_volume()
            self.player.audio_set_volume(volume + scale)

    def close(self):
        """Stops video playback and clears class values"""
        self.stop()
        self.instance = None
        self.media = None
        self.player = None

