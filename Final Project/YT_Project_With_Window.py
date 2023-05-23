import time
import vlc
import tkinter
import pafy


'''
url = "https://www.youtube.com/watch?v=W8SER24F0U8"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(playurl)
media.get_mrl()
player.set_media(media)
player.play()
time.sleep(50)
player.play()
'''

class Video:
    def __init__(self):
        self.new = 0
        self.file_in = open('youtube_links.txt', 'r')
        self.lines = self.file_in.readlines()
        self.url_list = []
        for link in self.lines:  # Adds the youtube links from the file to a list
            self.url_list.append(link.strip('\n'))

        self.file_in.close()
        #self.vid_num = 0

        self.main_window = tkinter.Tk()

        # Call video player
        self.url = self.url_list[0]
        self.video = pafy.new(self.url)
        self.best = self.video.getbest()
        self.playurl = self.best.url
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.playurl)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.video_set_scale(1.0)
        
        #self.player.play()
        #self.time.sleep(50)
        
        # Create frame
        self.mid_frame = tkinter.Frame(self.main_window)
        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.configure(bg='black')


        # Buttons in Mid frame

        self.play_btn = tkinter.Button(self.mid_frame, text="Play", command=self.play_vid, width=12)
        self.pause_btn = tkinter.Button(self.mid_frame, text="Pause", command=self.pause_vid, width=12)
        self.stop_btn = tkinter.Button(self.mid_frame, text="Stop", command=self.stop_vid, width=12)
        self.rewind_btn = tkinter.Button(self.mid_frame, text="Rewind", command=self.rewind_vid, width=12)
        self.fast_btn = tkinter.Button(self.mid_frame, text="Fast Forward", command=self.fast_vid, width=12)
        self.voldown_btn = tkinter.Button(self.mid_frame, text="Volume Down", command=self.vol_dwn, width=12)
        self.volup_btn = tkinter.Button(self.mid_frame, text="Volume Up", command=self.vol_up, width=12)

        if self.url_list[0]:
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", state=tkinter.DISABLED, width=12)
        else:
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", command=lambda: self.previous_vid(-1), width=12)

        self.next_btn = tkinter.Button(self.mid_frame, text="Next", command=lambda: self.next_vid(1), width=12)

        # Pack Buttons

        self.play_btn.grid(row=0, column=0)
        self.pause_btn.grid(row=0, column=1)
        self.stop_btn.grid(row=0, column=2)
        self.rewind_btn.grid(row=0, column=3)
        self.fast_btn.grid(row=0, column=4)
        self.voldown_btn.grid(row=0, column=5)
        self.volup_btn.grid(row=0, column=6)
        self.previous_btn.grid(row=0, column=7)
        self.next_btn.grid(row=0, column=8)


        # Pack Frames

        self.top_frame.grid(row=0, column=0, columnspan=8, padx=8)
        self.mid_frame.grid(row=1, column=0)


        tkinter.mainloop()


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
        self.value = self.player.get_position()

        self.player.set_position(self.value - 0.015)


    def fast_vid(self):
        # Rewind VLC Video
        self.value = self.player.get_position()

        self.player.set_position(self.value + 0.015)

    def vol_dwn(self):
        # Change Volume down
        self.volume = self.player.audio_get_volume()


        self.player.audio_set_volume(self.volume - 10)

    def vol_up(self):
        # Change Volume down
        self.volume = self.player.audio_get_volume()


        self.player.audio_set_volume(self.volume + 10)

    def next_vid(self, vid_num):

        global next_btn
        global previous_btn

        self.player.stop()
        self.url = self.url_list[vid_num]
        self.video = pafy.new(self.url)
        self.best = self.video.getbest()
        self.playurl = self.best.url
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.playurl)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.play()

        self.next_btn.grid_forget()
        self.previous_btn.grid_forget()
        try:
            self.next_btn = tkinter.Button(self.mid_frame, text="Next", command=lambda: self.next_vid(vid_num + 1), width=12)
            print(vid_num)
        except Exception:
            self.next_btn = tkinter.Button(self.mid_frame, text="Next", command=lambda: self.next_vid(vid_num + 2), width=12)

        try:
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", command=lambda: self.previous_vid(vid_num - 1), width=12)
            print(vid_num)
            print(len(self.url_list))
        except Exception:
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", command=lambda: self.previous_vid(vid_num - 2), width=12)


        if vid_num == len(self.url_list)- 1:
            self.next_btn = tkinter.Button(self.mid_frame, text="Next", state=tkinter.DISABLED, width=12)


        self.previous_btn.grid(row=0, column=7)
        self.next_btn.grid(row=0, column=8)



    def previous_vid(self, vid_num):
        global next_btn
        global previous_btn

        self.player.stop()
        self.url = self.url_list[vid_num]
        self.video = pafy.new(self.url)
        self.best = self.video.getbest()
        self.playurl = self.best.url
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.playurl)
        self.media.get_mrl()
        self.player.set_media(self.media)
        self.player.play()

        self.next_btn.grid_forget()
        self.previous_btn.grid_forget()

        try:
            self.next_btn = tkinter.Button(self.mid_frame, text="Next", command=lambda: self.next_vid(vid_num + 1), width=12)
            print(vid_num)
        except Exception:
            self.next_btn = tkinter.Button(self.mid_frame, text="Next", command=lambda: self.next_vid(vid_num + 2))

        try:
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", command=lambda: self.previous_vid(vid_num - 1), width=12)
            print(vid_num)
            print(len(self.url_list))
        except Exception:
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", command=lambda: self.previous_vid(vid_num - 2), width=12)

        if vid_num == 0:
            self.previous_btn = tkinter.Button(self.mid_frame, text="Prev", state=tkinter.DISABLED, width=12)

        self.previous_btn.grid(row=0, column=7)
        self.next_btn.grid(row=0, column=8)


play_ytube = Video()
