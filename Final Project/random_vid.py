"""
    Tim West, Programming Logic 105 - Final Project

    What does it do?
        Uses a tkinter GUI to get a users preferences on the random YouTube videos they want to see. It then uses those
        preferences to pull the correct videos from the YouTube API. The videos are then opened in the users default
        browser.

    What does it NOT do?
        It does not play YouTube videos within the GUI, nor does it download videos. The videos are also not
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
from YouTubeAPIError import YouTubeAPIError
from tkinter import *
from tkinter import messagebox
import webbrowser
import random

from YouTubeAPI import YouTubeAPI


class RandomVid:
    BUTTON_WIDTH = 18
    BUTTON_BG = 'gray'
    BUTTON_ACTIVE_BG = 'gray'

    """This class uses the YouTube API to open a top YouTube video given a category"""
    def __init__(self, api_key, local_player, root):
        # root
        self.root = root
        # Create Video class to display video locally
        self.local_player = local_player
        # Create frames
        self.setup_frames()
        # Setup buttons and labels for later
        self.setup_buttons_and_labels()
        # Call self.Category() to display buttons
        # self.category()
        self.youtube = YouTubeAPI(api_key)
        self.url_list = []
        self.run()

    def run(self):
        # Get the categories available
        my_dict = self.youtube.category()

        # Numbers could go up to 50, but I would advise sticking to at most 15
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        # Set the default option of the drop-down menu to "Categories" and the other to "Number Videos
        clicked = StringVar()
        clicked.set("Categories")

        results = IntVar()
        results.set("Number Videos")

        # Tell the user how to begin
        description_label = Label(self.top_frame,
                                  text='Choose a category and the number of videos you wish to view:',
                                  bg='gray', wraplength=300)
        description_label.grid(row=0, column=0, sticky=W)

        # Create a drop-down menu to have user make a selection
        category_drop = self.create_option_btn(self.mid_frame, clicked, my_dict.keys())
        num_videos = self.create_option_btn(self.mid_frame, results, numbers)

        # Enter Button
        enter_button = Button(self.mid_frame, text="Enter",
                              command=lambda: self.enter_action(my_dict, clicked, results),
                              bg='lightgreen', activebackground='lightgreen', width=18)
        # Add option menus and enter button to mid frame
        category_drop.grid(row=1, column=0, padx=10, pady=10)
        num_videos.grid(row=2, column=0, padx=10, pady=10)
        enter_button.grid(row=2, column=1, pady=10, padx=10)

    def enter_action(self, my_dict, clicked, results):
        try:
            self.url_list = self.youtube.link(my_dict, clicked, results)
        except (KeyError, TclError, YouTubeAPIError) as e:
            print(f"Error, {str(e)} ")
            messagebox.showwarning('Error', "Please select from the drop down menus, then hit enter!")
        else:
            self._vid_opener()

    def _vid_opener(self):
        options = ['Randomize', 'Most Popular First', 'Least Popular First']

        selected = StringVar()
        selected.set('Randomize')

        # Label and menu button for video play back
        play_label = Label(self.play_frame, text='Choose the order you want the videos played:', bg='gray')
        play_label.grid(row=0, column=0)

        # Menu Option Button #1
        playback_menu = self.create_option_btn(self.status_frame, selected, options)
        playback_menu.grid(row=1, column=0, padx=10, pady=10)
        options = StringVar()
        options.set("Options")
        option_list = ['Open All', 'Open on Click', 'Play Locally']
        # Menu Option Button #2
        option_btn2 = self.create_option_btn(self.status_frame, options, option_list)
        option_btn2.grid(row=2, column=0, padx=10, pady=10)
        # Green Enter Button
        enter_button = Button(self.status_frame, text="Enter",
                              command=lambda: self.get_options(selected, self.url_list, options, self.url_list),
                              bg='lightgreen', activebackground='lightgreen', width=self.BUTTON_WIDTH)
        enter_button.grid(row=2, column=1, pady=10, padx=10)

    def get_options(self, select, urls, option, urls2):  # Takes users selected options and continues depending on them
        choice = select.get()
        options = option.get()

        if options != 'Options':
            url_order = RandomVid.get_url_order(choice, urls, urls2)

            self.notice_label.grid_forget()
            self.update_label.grid_forget()

            if options == 'Open All':
                self.destroy_default_buttons()
                RandomVid.all_in_browser(url_order)
                self.notice_label.config(text='All videos have been opened in the default browser.')

            elif options == 'Open on Click':
                # If you play on click the order the videos open is different from all at once
                self.setup_buttons(url_order, 0)
                self.notice_label.config(text='Click the \"next\" and \"prev\" buttons to change videos.')

            elif options == 'Play Locally':
                self.destroy_default_buttons()
                # Opens the local tkinter window that has VLC media player embedded in it
                self.notice_label.config(text='Video are playing in a local tkinter with VLC media player embedded. '
                                         'Make use of previous and next buttons to advanced to a video.')
                self.play_locally(url_order)
            # Add Labels to view
            self.update_label.grid(row=5, column=0, sticky=E + W)
            self.notice_label.grid(row=6, column=0, sticky=E + W)
        else:
            messagebox.showwarning('Error', 'Please select from the drop down menus, then hit enter!')

    def play_locally(self, url_list):
        self.local_player.open_window(url_list)

    def setup_buttons(self, urls, num):
        new = 0
        current_vid = urls[num]
        webbrowser.open(current_vid, new=new)
        # Need to forget the previous buttons\labels to not mess up new buttons\labels
        self.destroy_default_buttons()  # Must destroy them here so that they are properly forgotten
        self.setup_buttons_and_labels()
        # Create status bar and next/prev buttons
        self.status.config(text='Video ' + str(num + 1) + ' of ' + str(len(urls)), relief=SUNKEN, width=16)

        # If it is the last video do not want to keep going, so disable next
        if urls[num] == urls[len(urls) - 1]:
            self.next_btn.config(state=DISABLED, bg='red', width=8)
        else:
            self.next_btn.config(command=lambda: self.setup_buttons(urls, num + 1), bg='cyan', width=8)

        # If it's the first video do not want to go backwards
        if urls[num] == urls[0]:
            self.prev_btn.config(state=DISABLED, bg='red', width=8)
        else:
            self.prev_btn.config(command=lambda: self.setup_buttons(urls, num - 1), bg='pink', width=8)

        # Place the buttons and label onto a grid
        self.prev_btn.grid(row=4, column=0, sticky=W, pady=5, padx=10)
        self.status.grid(row=4, column=1, sticky=E + W, padx=5, ipadx=4)
        self.next_btn.grid(row=4, column=2, sticky=E, pady=5, padx=10)

    def setup_frames(self):
        self.top_frame = RandomVid.create_frame(self.root, 'gray')
        self.mid_frame = RandomVid.create_frame(self.root, 'darkgray', padx=36)
        self.play_frame = RandomVid.create_frame(self.root, 'gray')
        self.status_frame = RandomVid.create_frame(self.root, 'darkgray', padx=36)
        self.next_frame = RandomVid.create_frame(self.root, 'gray')
        self.bot_frame = RandomVid.create_frame(self.root, 'gray')

    def setup_buttons_and_labels(self):
        # Need to initialize buttons/ labels for later use
        self.next_btn = self.create_button(self.next_frame, text="Next")
        self.prev_btn = self.create_button(self.next_frame, text="Prev")
        self.status = Label(self.next_frame)
        self.update_label = Label(self.bot_frame, text="Your videos will open shortly.", bg='gray')
        self.notice_label = Label(self.bot_frame, bg='gray', wraplength=250)

    def destroy_default_buttons(self):
        self.next_btn.destroy()
        self.prev_btn.destroy()
        self.status.destroy()

    def create_option_btn(self, parent, options, option_list):
        default_option_btn = OptionMenu(parent, options, *option_list)
        default_option_btn.config(width=self.BUTTON_WIDTH, bg=self.BUTTON_BG, activebackground=self.BUTTON_ACTIVE_BG)
        return default_option_btn

    def create_button(self, parent, **kwargs):
        default_btn = {'width': self.BUTTON_WIDTH, 'bg': self.BUTTON_BG, 'activebackground': self.BUTTON_ACTIVE_BG}
        default_btn.update(kwargs)
        return Button(parent, **default_btn)

    @staticmethod
    def all_in_browser(urls):
        for links in urls:  # Opens the links in default web browser
            webbrowser.open(links, new=0)

    @staticmethod
    def create_frame(root, color, **kwargs):
        frame = Frame(root)
        frame.configure(bg=color, **kwargs)
        frame.pack(side='top')
        return frame

    @staticmethod
    def get_url_order(choice, urls, urls2):
        if choice == 'Randomize':
            random.shuffle(urls2)
            return urls2
        elif choice == 'Least Popular First':
            urls = urls[::-1]
        return urls
