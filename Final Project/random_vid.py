from googleapiclient.discovery import build
from tkinter import *
from tkinter import messagebox
import webbrowser
import random


class RandomVid:
    BUTTON_WIDTH = 18
    BUTTON_BG = 'gray'
    BUTTON_ACTIVE_BG = 'gray'

    """This class uses the YouTube API to open a top YouTube video given a category"""
    def __init__(self, api_key, local_player, root):
        # root
        self.root = root
        # Initialize Api key
        self.api_key = api_key
        # Create Video class to display video locally
        self.local_player = local_player
        # Create frames
        self.setup_frames()
        # Setup buttons and labels for later
        self.setup_buttons_and_labels()
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
            with open('youtube_links.txt', 'w') as file:  # Writes the links to a file
                for ids in vid_list:
                    vids = f'https://www.youtube.com/watch?v={ids}'  # Inserts video ids into a YouTube link
                    file.write(vids + '\n')
            file.close()
            # Makes next set of menus pop up in window
            self.vid_opener()

    def vid_opener(self):
        # Adds the YouTube links from the file to a list
        with open('youtube_links.txt', 'r') as file_in:
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
                              command=lambda: self.get_options(selected, url_list, options, url_list),
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
