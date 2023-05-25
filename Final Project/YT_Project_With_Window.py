import vlc
import tkinter
import pafy


class Video:
    def __init__(self):
        self.vid_num = 0
        # Call video player
        self.root = None
        self.url_list = None
        self.player = None
        self.instance = None
        self.media = None

    def open_window(self, url_list):
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
            # Buttons in Mid frame
            self.play_btn = tkinter.Button(self.mid_frame, text="Play", command=self.play_vid, width=12)
            self.pause_btn = tkinter.Button(self.mid_frame, text="Pause", command=self.pause_vid, width=12)
            self.stop_btn = tkinter.Button(self.mid_frame, text="Stop", command=self.stop_vid, width=12)
            self.rewind_btn = tkinter.Button(self.mid_frame, text="Rewind", command=self.rewind_vid, width=12)
            self.fast_btn = tkinter.Button(self.mid_frame, text="Fast Forward", command=self.fast_vid, width=12)
            self.voldown_btn = tkinter.Button(self.mid_frame, text="Volume Down", command=self.vol_dwn, width=12)
            self.volup_btn = tkinter.Button(self.mid_frame, text="Volume Up", command=self.vol_up, width=12)
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", state=tkinter.DISABLED, width=12)
            self.next_btn = tkinter.Button(self.mid_frame, text="Next", command=lambda: self.next_vid(), width=12)
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

        self.update_list(url_list)

    def update_list(self, urls):
        self.url_list = []
        self.url_list = urls
        self.vid_num = 0
        if self.player is not None:
            self.player.stop()
        if urls is not None and len(urls) > 0:
            self.get_player()

    def play_vid(self):
        # Play VLC Video
        self.player.play()

    def pause_vid(self):
        # Pause VLC Video
        self.player.set_pause(1)

    def stop_vid(self):
        # Stop VLC Video
        self.player.stop()

    def rewind_vid(self):
        # Rewind VLC Video
        self.player.set_position(self.player.get_position() - 0.015)

    def fast_vid(self):
        # Rewind VLC Video
        self.player.set_position(self.player.get_position() + 0.015)

    def vol_dwn(self):
        # Change Volume down
        volume = self.player.audio_get_volume()
        self.player.audio_set_volume(volume - 10)

    def vol_up(self):
        # Change Volume down
        volume = self.player.audio_get_volume()
        self.player.audio_set_volume(volume + 10)

    def next_vid(self):
        self.vid_num += 1
        # Puts next video into the player
        self.get_player()

    def previous_vid(self):
        self.vid_num -= 1
        # Puts previous video into the player
        self.get_player()

    def set_buttons(self):
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

    def get_player(self):
        if self.instance is None:
            self.instance = vlc.Instance()
            self.player = self.instance.media_player_new()
            self.win_id = self.main_window.winfo_id()
            self.player.set_hwnd(self.win_id)

        self.url = self.url_list[self.vid_num]
        self.video = pafy.new(self.url)
        self.best = self.video.getbest()
        self.playurl = self.best.url
        self.media = self.instance.media_new(self.playurl)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.video_set_scale(0)
        self.player.play()
        self.set_buttons()

    def on_close(self):
        self.stop_vid()
        self.root.destroy()
        self.root = None
        self.url_list = None
        self.player = None
        self.instance = None
        self.media = None
