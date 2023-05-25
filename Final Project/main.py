import os
from YT_Project_With_Window import Video
from DestroyableTk import DestroyableTK
from YT_final_project import RandomVid

# Program starts here
if __name__ == '__main__':
    video = Video()
    root = DestroyableTK(video)
    root.title("Random YouTube Video?")  # This is title of program
    root.iconbitmap('C:/Users/Tim/Documents/GitHub/YouTube-Python-Project/Project_imgs/youtube_button.ico')
    root.geometry("400x400")
    root.configure(bg='gray')
    root.resizable(False, False)

    # Api key is stored as an environment variable, don't share your api key!
    youtube_key = os.environ.get('YT_KEY')

    youtube_vid = RandomVid(youtube_key, video, root)
    root.mainloop()
