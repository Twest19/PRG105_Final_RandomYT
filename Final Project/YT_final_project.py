"""
    Tim West, Programming Logic 105 - Final Project

    What does it do?
        Uses a tkinter GUI to get a users preferences on the random YouTube videos they want to see. It then uses those
        preferences to pull the correct videos from the YouTube API. The videos are then opened in the users default
        browser.

    What does it NOT do?
        It does not play play YouTube videos within the GUI, nor does it download videos. The videos are also not
        necessarily random, rather they are pulled from the most popular videos in each category for the day. All
        controls over the video like volume, playback speed, and quality will still be handled via YouTube itself.
        This is just merely a video opener.

    Requirements for use ----
        pip install --upgrade google-api-python-client
        pip install tk

        You will also NEED to get your own YouTube API key. Without it the program will not work! It is completely
        free, you just need to create a Google account. DO NOT SHARE YOUR API KEY! I have put mine in an environment
        variable so that others can not access it. I would recommend you do so as well! There is also a limit per day
        on the number of requests you can send to the YouTube API. The limit for free accounts is 10,000 quota a day.
        This program only uses about 2-3 quota per use, so you should never hit that limit.

        You can find out more about this here:
        https://developers.google.com/youtube/v3/getting-started
        and here:
        https://developers.google.com/youtube/v3/quickstart/python

        I would also like to recommend that you have a YouTube account. YouTube sometimes has age restrictions on
        videos, thus requiring a YouTube account.

    How to use it?
        A simple graphical user interface window will appear. At the top of the window you will see a text label that
        asks you to choose a video category and the number of videos you want to see. The categories are inside a drop
        down menu, as are the number of videos. The number of videos option is just giving you the option to play
        anywhere from 1 - 15 videos. Later on you will be able to select if you want the videos to open all at once,
        or open via a next button. Make sure to hit enter to submit your choices, if you do not the program will go no
        further! Also if you hit enter without making a choice in one of the boxes, it will pop up a message window
        telling you to make a selection.

        After you have hit enter a new set of drop down menus will appear. These menus will give you the option of how
        you want the videos to appear. The first box that says "Randomize" has several options for what order the
        videos should play in. "Randomize" will randomize the order, "Most Popular First" will play the most popular
        video first, and "Least Popular First" will play the least most popular video first. The "Options" menu gives
        you the choice of "Open All" which will open all the videos at once in your browser, or "Open on Click" which
        will open the first video automatically and then consecutive videos will be opened by clicking the next button
        or previous buttons.

        Your videos should now have been opened in your default web browser. You will now have full control over them
        just as if you were watching YouTube normally. Also if you choose the "Open All" option it may or may not play
        the videos back in the correct order. This is can happen when one video is loaded into the browser faster than
        another. Unfortunately there is not much that can be done about that, except for choosing "Open on Click".

    Resources ---

        YouTube API links/Resources:
            https://developers.google.com/youtube
            https://developers.google.com/youtube/v3/getting-started
            https://developers.google.com/youtube/v3/quickstart/python
            https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md
            https://github.com/googleapis/google-api-python-client/blob/master/docs/README.md
            https://github.com/youtube/api-samples
            https://github.com/youtube/api-samples/blob/master/python/README.md


        Tutorials that helped me get started with the YouTube API:
            Corey Schafer: Python YouTube API Tutorial: Getting Started
                https://www.youtube.com/watch?v=th5_9woFJmk&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=3
            Corey Schafer: Python YouTube API Tutorial: Calculating the Duration of a Playlist
                https://www.youtube.com/watch?v=coZbOM6E47I&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=3

        Tkinter GUI Resources:
            freecodecamp.org Tkinter course
                https://youtu.be/YXPyB4XeYLA

        Webbrowser Python Resources:
            https://docs.python.org/3/library/webbrowser.html

        Python Random:
            https://docs.python.org/3/library/random.html

        Python os:
            https://docs.python.org/3/library/os.html

"""
import os
from googleapiclient.discovery import build
from tkinter import *
from tkinter import messagebox
import webbrowser
import random


class RandomVid:
    """This class uses the YouTube API to open a top YouTube video given a category"""
    def __init__(self, api_key):
        # Initialize Api key
        self.api_key = api_key

        # Create frames
        self.top_frame = Frame(root)
        self.top_frame.configure(bg='gray')

        self.mid_frame = Frame(root)
        self.mid_frame.configure(bg='darkgray', padx=36)

        self.play_frame = Frame(root)
        self.play_frame.configure(bg='gray')

        self.status_frame = Frame(root)
        self.status_frame.configure(bg='darkgray', padx=36)

        self.next_frame = Frame(root)
        self.next_frame.configure(bg='gray')

        self.bot_frame = Frame(root)
        self.bot_frame.configure(bg='gray')

        # Need to initialize buttons/ labels for later use
        self.next_btn = Button(self.next_frame)
        self.prev_btn = Button(self.next_frame)
        self.status = Label(self.next_frame)

        # Put frames on screen
        self.top_frame.pack(side='top')
        self.mid_frame.pack(side='top')
        self.play_frame.pack(side='top')
        self.status_frame.pack(side='top')
        self.next_frame.pack(side='top')
        self.bot_frame.pack(side='top')

        # Call self.Category() to display buttons
        self.category()

    def category(self):
        # This is where we will contact the YouTube API to get the category names and ids
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        request = youtube.videoCategories().list(
            part='snippet',
            regionCode='US'
        )

        response_one = request.execute()  # Execute the youtube api request for categories

        # Add the categories and category ids to dictionary, should update if YouTube adds any new ones
        my_dict = {}
        for item in response_one['items']:
            if item['snippet']['assignable'] is False:
                pass
            else:
                tube_dict1 = item['snippet']['title']
                tube_dict2 = item['id']
                my_dict[tube_dict1] = tube_dict2

        # The Trending category will need to be added manually here
        my_dict['Trending'] = '0'

        # The Travel category does not work, so needs to be removed
        del my_dict['Travel & Events']

        # Numbers could go up to 50, but I would advise to stick to at most 15
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        # Set the default option of the drop down menu to "Categories" and the other to "Number Videos
        clicked = StringVar()
        clicked.set("Categories")

        results = IntVar()
        results.set("Number Videos")

        # Tell the user how to begin
        description_label = Label(self.top_frame,
                                  text='Choose a category and the number of videos you wish to view:',
                                  bg='gray', wraplength=300)
        description_label.grid(row=0, column=0, sticky=W)

        # Create a drop down menu to have user make a selection
        category_drop = OptionMenu(self.mid_frame, clicked, *my_dict.keys())
        category_drop.config(width=18, bg='gray', activebackground='gray')

        num_videos = OptionMenu(self.mid_frame, results, *numbers)
        num_videos.config(width=18, bg='gray', activebackground='gray')

        enter_button = Button(self.mid_frame, text="Enter", command=lambda: self.get_link(my_dict, clicked, results),
                              bg='lightgreen', activebackground='lightgreen', width=18)

        # Add option menus and enter button to mid frame
        category_drop.grid(row=1, column=0, padx=10, pady=10)
        num_videos.grid(row=2, column=0, padx=10, pady=10)
        enter_button.grid(row=2, column=1, pady=10, padx=10)

    def get_link(self, my_dict, click, num):
        try:
            result = num.get()
            clicked_label = click.get()
            youtube = build('youtube', 'v3', developerKey=self.api_key)

            # Uses selected category to get video ids from the YouTube API
            request = youtube.videos().list(
                part='snippet,contentDetails,statistics',
                chart='mostPopular',
                regionCode='US',
                videoCategoryId=my_dict[clicked_label],
                maxResults=result
            )

            vid_list = []

            response_two = request.execute()

            for item in response_two['items']:  # Saves video ids to a list
                vid_list.append(item['id'])

        except (KeyError, TclError):
            messagebox.showwarning('Error', 'Please select from the drop down menus, then hit enter!')

        else:
            file = open('youtube_links.txt', 'w')  # Writes the links to a file
            for ids in vid_list:
                vids = f'https://www.youtube.com/watch?v={ids}'  # Inserts video ids into a youtube link
                file.write(vids + '\n')
            file.close()
            self.vid_opener()

    def vid_opener(self):
        # Adds the youtube links from the file to a list
        file_in = open('youtube_links.txt', 'r')
        lines = file_in.readlines()

        url_list = []
        url_list2 = []

        for url in lines:
            url_list.append(url.strip('\n'))
            url_list2.append(url.strip('\n'))

        file_in.close()

        options = ['Randomize', 'Most Popular First', 'Least Popular First']

        selected = StringVar()
        selected.set('Randomize')

        # Label and menu button for video play back
        play_label = Label(self.play_frame, text='Choose the order you want the videos played:', bg='gray')
        play_label.grid(row=0, column=0)

        playback_menu = OptionMenu(self.status_frame, selected, *options)
        playback_menu.config(width=18, bg='gray', activebackground='gray')
        playback_menu.grid(row=1, column=0, padx=10, pady=10)

        options = StringVar()
        options.set("Options")

        option_list = ['Open All', 'Open on Click']

        option_btn2 = OptionMenu(self.status_frame, options, *option_list)
        option_btn2.config(width=18, bg='gray', activebackground='gray')
        option_btn2.grid(row=2, column=0, padx=10, pady=10)

        enter_button = Button(self.status_frame, text="Enter",
                              command=lambda: self.get_options(selected, url_list, options, url_list),
                              bg='lightgreen', activebackground='lightgreen', width=18)
        enter_button.grid(row=2, column=1, pady=10, padx=10)

    def get_options(self, select, urls, option, urls2):  # Takes users selected options and continues depending on them
        new = 0
        choice = select.get()
        options = option.get()
        if options != 'Options':
            if options == 'Open All':
                self.next_btn.grid_forget()
                self.prev_btn.grid_forget()
                self.status.grid_forget()
                # If you play on click the order the videos open is different than all at once
                if choice == 'Randomize':
                    random.shuffle(urls2)
                    for links in urls2:  # Need to use a different list here since it will shuffle the urls
                        webbrowser.open(links, new=new)

                elif choice == 'Most Popular First' or 'Least Popular First':
                    if choice == 'Most Popular First':
                        urls = urls[::-1]
                    elif choice == 'Least Popular First':
                        pass

                    for links in urls:  # Opens the links in default web browser
                        webbrowser.open(links, new=new)

            elif options == 'Open on Click':
                # If you play on click the order the videos open is different than all at once
                if choice == 'Randomize':
                    random.shuffle(urls2)
                    webbrowser.open(urls2[0], new=new)
                elif choice == 'Most Popular First' or 'Least Popular First':
                    if choice == 'Most Popular First':
                        pass
                    elif choice == 'Least Popular First':
                        urls = urls[::-1]

                    # Opens the links in default web browser
                    webbrowser.open(urls[0], new=new)

                # Create next and previous buttons
                self.next_btn = Button(self.next_frame, text='Next',
                                       command=lambda: self.next_vid(urls, 1), bg='cyan', width=8)

                # Do not want to go backwards at first video
                if urls[0]:
                    self.prev_btn = Button(self.next_frame, text="Prev", state=DISABLED, bg='red', width=8)
                else:
                    self.prev_btn = Button(self.next_frame, text='Prev',
                                           command=lambda: self.prev_vid(urls, 1), bg='pink', width=8)

                # Create a status bar to display what number video is playing
                self.status = Label(self.next_frame, text='Video 1 of ' + str(len(urls)),
                                    relief=SUNKEN, width=16)

                # Put Buttons on the screen
                self.next_btn.grid(row=4, column=2, sticky=E, pady=5, padx=10)
                self.status.grid(row=4, column=1, sticky=E + W, padx=5, ipadx=4)
                self.prev_btn.grid(row=4, column=0, sticky=W, pady=5, padx=10)

            update_label = Label(self.bot_frame, text="Your videos will open shortly.", bg='gray')
            notice_label = Label(self.bot_frame,
                                 text='*Please note that the "Open All" option may not open all of the videos in '
                                      'the correct order. '
                                      'This is due to varying factors out of the programs control.',
                                 bg='gray', wraplength=250)

            update_label.grid(row=5, column=0, sticky=E + W)
            notice_label.grid(row=6, column=0, sticky=E + W)
        else:
            messagebox.showwarning('Error', 'Please select from the drop down menus, then hit enter!')

    def next_vid(self, urls, num):  # Allows for a next video to be played
        new = 0
        current_vid = urls[num]

        webbrowser.open(current_vid, new=new)

        # Need to forget the previous buttons so new ones can be applied
        self.next_btn.grid_forget()
        self.prev_btn.grid_forget()
        self.status.grid_forget()

        # Create status bar and next/prev buttons
        self.status = Label(self.next_frame, text='Video ' + str(num + 1) + ' of ' + str(len(urls)),
                            relief=SUNKEN, width=16)

        # If it is the last video do not want to keep going, so disable next
        if urls[num] == urls[len(urls) - 1]:
            self.next_btn = Button(self.next_frame, text="Next", state=DISABLED, bg='red', width=8)
        else:
            self.next_btn = Button(self.next_frame, text='Next',
                                   command=lambda: self.next_vid(urls, num + 1), bg='cyan', width=8)

        self.prev_btn = Button(self.next_frame, text='Prev',
                               command=lambda: self.prev_vid(urls, num - 1), bg='pink', width=8)

        # Place the buttons and label onto a grid
        self.next_btn.grid(row=4, column=2, sticky=E, pady=5, padx=10)
        self.status.grid(row=4, column=1, sticky=E + W, padx=5, ipadx=4)
        self.prev_btn.grid(row=4, column=0, sticky=W, pady=5, padx=10)

    def prev_vid(self, urls, num):  # Allows for a previous video to be played
        new = 0

        current_vid = urls[num]

        webbrowser.open(current_vid, new=new)

        # Need to forget the previous buttons\labels to not mess up new buttons\labels
        self.next_btn.grid_forget()
        self.prev_btn.grid_forget()
        self.status.grid_forget()

        # Create status bar and next/prev buttons
        self.status = Label(self.next_frame, text='Video ' + str(num + 1) + ' of ' + str(len(urls)),
                            relief=SUNKEN, width=16)

        self.next_btn = Button(self.next_frame, text='Next',
                               command=lambda: self.next_vid(urls, num + 1), bg='cyan', width=8)
        self.prev_btn = Button(self.next_frame, text='Prev',
                               command=lambda: self.prev_vid(urls, num - 1), bg='pink', width=8)

        # If its the first video do not want to go backwards
        if urls[num] == urls[0]:
            self.prev_btn = Button(self.next_frame, text="Prev", state=DISABLED, bg='red', width=8)

        # Place the buttons and label onto a grid
        self.prev_btn.grid(row=4, column=0, sticky=W, padx=10, pady=5)
        self.status.grid(row=4, column=1, sticky=E + W, ipadx=4)
        self.next_btn.grid(row=4, column=2, sticky=E, padx=10, pady=5)


# Program starts here
if __name__ == '__main__':
    root = Tk()
    root.title("Random YouTube Video?")  # This is title of program
    root.iconbitmap('C:/Users/white/Desktop/YouTube Python Project/Project_imgs/youtube_button.ico')
    root.geometry("400x400")
    root.configure(bg='gray')
    root.resizable(False, False)

    # Api key is stored as an environment variable, don't share your api key!
    youtube_key = os.environ.get('YT_KEY')

    youtube_vid = RandomVid(youtube_key)
    root.mainloop()
