import tkinter
from vlc_player import VlcPlayer


class Video:
    """
        This class is responsible for managing and controlling video playback.
    """
    DEFAULT_BTN_WIDTH = 12
    DEFAULT_BUTTON_BG = 'white'
    DEFAULT_BUTTON_ACTIVE_BG = 'white'
    DEFAULT_REWIND_FF_SCALE = 0.015
    DEFAULT_AUDIO_SCALE = 10
    DEFAULT_PLAY_BAR_ROW = 0

    def __init__(self):
        self.vid_num = 0
        # init require video variables
        self.root = None
        self.url_list = None
        self.player = VlcPlayer()

    def open_window(self, url_list):
        """ Responsible for setting up UI elements, especially the root tkinter window.
        Also, updates the list of urls for playback. Generally, this is called to make the window appear, this way,
        the window will not open upon initializing a Video instance."""
        self.setup_ui()
        self.update_list(url_list)

    def get_player(self):
        """Creates the player for viewing content locally, setting up the window and it's buttons"""
        self.url = self.url_list[self.vid_num]
        self.win_id = self.main_window.winfo_id()
        self.player.create_instance(self.win_id, self.url)
        self.player.play()
        self.set_buttons()

    def update_list(self, urls):
        """ Updates hte list of URLs, stops the video player if a video is in progress,
        and updates player to next video """
        self.url_list = []
        self.url_list = urls
        self.vid_num = 0
        if urls is not None and len(urls) > 0:
            self.get_player()

    def setup_ui(self):
        """ Create the basic UI elements, given that the root tkinter window has not already been created. """
        if self.root is None:
            self.root = tkinter.Tk()
            self.root.protocol("WM_DELETE_WINDOW", self.on_close)
            # Window setup
            self.root.geometry("900x600")
            # Create frame
            self.main_window = tkinter.Frame(self.root, bg="black")
            self.mid_frame = tkinter.Frame(self.root)
            self.top_frame = tkinter.Frame(self.root, bg='black')
            # Pack Frames
            self.top_frame.grid(row=0, column=0, columnspan=8, sticky='ew', padx=8)
            self.mid_frame.grid(row=1, column=0, sticky='ew')
            self.main_window.grid(row=2, column=0, sticky='nsew')
            self.root.grid_rowconfigure(2, weight=1)
            self.root.grid_columnconfigure(0, weight=1)
            # Create Playback Buttons
            self.create_playback_bar()

    def create_playback_bar(self):
        """ Creates and setup UI elements pertaining to the video playback bar, like play, rewind, next buttons. """
        # Buttons in Mid frame
        self.play_btn = self.default_button(self.mid_frame, text="Play", command=self.play_vid)
        self.pause_btn = self.default_button(self.mid_frame, text="Pause", command=self.pause_vid)
        self.stop_btn = self.default_button(self.mid_frame, text="Stop", command=self.stop_vid)
        self.rewind_btn = self.default_button(self.mid_frame, text="Rewind", command=self.rewind_vid)
        self.fast_btn = self.default_button(self.mid_frame, text="Fast Forward", command=self.fast_vid)
        self.voldown_btn = self.default_button(self.mid_frame, text="Volume Down", command=self.vol_dwn)
        self.volup_btn = self.default_button(self.mid_frame, text="Volume Up", command=self.vol_up)
        self.previous_btn = self.default_button(self.mid_frame, text="Prev", state=tkinter.DISABLED)
        self.next_btn = self.default_button(self.mid_frame, text="Next", command=lambda: self.next_vid())
        # Grid Buttons
        pad_x = (900 - (12 * 9 * 8)) // 2  # 12 (width) * 9 (num of buttons) * 8 (approx pixels per char)
        self.play_btn.grid(row=0, column=0, padx=(pad_x, 0))
        self.pause_btn.grid(row=0, column=1)
        self.stop_btn.grid(row=0, column=2)
        self.rewind_btn.grid(row=0, column=3)
        self.fast_btn.grid(row=0, column=4)
        self.voldown_btn.grid(row=0, column=5)
        self.volup_btn.grid(row=0, column=6)
        self.previous_btn.grid(row=0, column=7)
        self.next_btn.grid(row=0, column=8, padx=(0, pad_x))

    def default_button(self, parent, **kwargs):
        """ Method for creating a button that uses the default properties making changing size and color easier. """
        default_btn = {'width': self.DEFAULT_BTN_WIDTH,
                       'bg': self.DEFAULT_BUTTON_BG,
                       'activebackground': self.DEFAULT_BUTTON_ACTIVE_BG}
        default_btn.update(kwargs)
        return tkinter.Button(parent, **default_btn)

    def set_buttons(self):
        """Set the state of buttons and configures them as needed"""
        # Disable next button if at last video
        if self.vid_num == len(self.url_list) - 1:
            self.next_btn.configure(state=tkinter.DISABLED)
        else:
            self.next_btn.configure(state=tkinter.NORMAL)

        # Disable previous button if at first video
        if self.vid_num == 0:
            self.previous_btn.configure(state=tkinter.DISABLED)
        else:
            self.previous_btn.configure(state=tkinter.NORMAL)

        self.next_btn.configure(command=lambda: self.next_vid())
        self.previous_btn.configure(command=lambda: self.previous_vid())

    def play_vid(self):
        """Play VLC Video"""
        self.player.play()

    def pause_vid(self):
        """Pause VLC Video"""
        self.player.pause()

    def stop_vid(self):
        """Stop VLC Video"""
        self.player.stop()

    def rewind_vid(self):
        """Rewind VLC Video"""
        self.player.rewind(self.DEFAULT_REWIND_FF_SCALE)

    def fast_vid(self):
        """Rewind VLC Video"""
        self.player.fast(self.DEFAULT_REWIND_FF_SCALE)

    def vol_dwn(self):
        """Change Volume Down"""
        self.player.volume_down(self.DEFAULT_AUDIO_SCALE)

    def vol_up(self):
        """Change Volume Up"""
        self.player.volume_up(self.DEFAULT_AUDIO_SCALE)

    def next_vid(self):
        """Changes to next video in list"""
        self.vid_num += 1
        # Puts next video into the player
        self.get_player()

    def previous_vid(self):
        """Changes to previous video in list"""
        self.vid_num -= 1
        # Puts previous video into the player
        self.get_player()

    def on_close(self):
        """Responsible for stopping video playback, resetting values, and destroying tkinter window"""
        self.player.close()
        self.root.destroy()
        self.root = None
        self.url_list = None
