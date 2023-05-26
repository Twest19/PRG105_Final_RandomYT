import os
from video import Video
from destroyable_tk import DestroyableTK
from random_vid import RandomVid

# Program starts here
"""
Program starts here. It requires a YouTube API Key and the proper modules to be installed to work.
Packages required:
    python-vlc:
    youtube-dl
    pafy
    googleapiclient
    tkinter

    Note: VLC Media player must also be installed for functionality, free download can be found here: VLC Media Player. 
    Make sure you download the proper 32 or 64 bit version, errors may arise if you do not. 
    Missing \'libvlc.dll\' is one errors that can occur if 32bit VLC media player is installed on a 64bit system.
    Unsure of if you have a 32 or 64bit? On windows go to start, type \"About your PC\" click the corresponding option. 
    From there you should be able to find out where it says \"System Type\" 
    EX: System Type 64-bit operating system, x64-based processor

"""
if __name__ == '__main__':
    video = Video()
    root = DestroyableTK(video)
    root.title("Random YouTube Video?")  # This is title of program
    current_dir = os.path.dirname(os.path.realpath(__file__))
    icon_path = os.path.join(current_dir, 'youtube_button.ico')
    root.iconbitmap(icon_path)
    root.geometry("400x400")
    root.configure(bg='gray')
    root.resizable(False, False)

    # Api key is stored as an environment variable, don't share your api key! Search online for more info about this.
    try:
        youtube_key = os.environ.get('YT_KEY')
        if youtube_key is None:
            raise ValueError("Environment variable 'YT_KEY' is not set.")
        youtube_vid = RandomVid(youtube_key, video, root)
    except ValueError as e:
        print("ERROR: YouTube API key not found. Please set the environment variable 'YT_KEY'.")
        print(e)
        exit(1)  # Exit with a status code indicating an error

    root.mainloop()
