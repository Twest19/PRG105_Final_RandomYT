import tkinter as tk


class DestroyableTK(tk.Tk):
    def __init__(self, local_player, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.local_player = local_player
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # If video is playing stop it
        try:
            self.local_player.player.stop()
        except Exception as e:
            print(f'Error in stopping the video player: {e}')
        self.destroy()
