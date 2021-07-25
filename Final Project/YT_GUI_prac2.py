import os
from googleapiclient.discovery import build
from tkinter import *
from tkinter import messagebox
import webbrowser
import random


class RandomVid:
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

    def get_link(self, my_dict, click, num):
        try:
            result = num.get()
            clicked_label = click.get()
            youtube = build('youtube', 'v3', developerKey=self.api_key)

            # Uses selected category to get video ids from
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

    def category(self):

        youtube = build('youtube', 'v3', developerKey=self.api_key)
        request = youtube.videoCategories().list(
            part='snippet',
            regionCode='US'
        )

        response_one = request.execute()  # Execute the youtube api request for categories

        # Add the categories and category ids to dictionary
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
        del my_dict['Travel & Events']

        # Numbers could go up to 50, but I would advise to stick to at most 15
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        # Set the default option of the drop down menu to "Categories"
        clicked = StringVar()
        clicked.set("Categories")

        results = IntVar()
        results.set("Number Videos")

        # Tell user what program does
        description_label = Label(self.top_frame,
                                  text='Choose a category and the number of videos you wish to view:',
                                  bg='gray', wraplength=300)
        description_label.grid(row=0, column=0, sticky=W)

        # Create a drop down menu to have user make a selection
        category_drop = OptionMenu(self.mid_frame, clicked, *my_dict.keys())
        category_drop.config(width=18, bg='gray', activebackground='gray')
        category_drop.grid(row=1, column=0, padx=10, pady=10)

        num_videos = OptionMenu(self.mid_frame, results, *numbers)
        num_videos.config(width=18, bg='gray', activebackground='gray')
        num_videos.grid(row=2, column=0, padx=10, pady=10)

        enter_button = Button(self.mid_frame, text="Enter", command=lambda: self.get_link(my_dict, clicked, results),
                              bg='lightgreen', activebackground='lightgreen', width=18)
        enter_button.grid(row=2, column=1, pady=10, padx=10)

    def get_options(self, select, urls, option):
        new = 0
        choice = select.get()
        options = option.get()
        try:
            if options == 'Open all':
                # If you play on click the order the videos open is different than all at once
                if choice == 'Randomize':
                    random.shuffle(urls)
                elif choice == 'Most Popular First':
                    urls.reverse()
                elif choice == 'Least Popular First':
                    pass

                for links in urls:  # Opens the links in default web browser
                    webbrowser.open(links, new=new)

                self.next_btn.grid_forget()
                self.prev_btn.grid_forget()
                self.status.grid_forget()

            elif options == 'Open when clicked':
                # If you play on click the order the videos open is different than all at once
                if choice == 'Randomize':
                    random.shuffle(urls)
                elif choice == 'Most Popular First':
                    pass
                elif choice == 'Least Popular First':
                    urls.reverse()

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

                self.next_btn.grid(row=4, column=2, sticky=E, pady=5, padx=10)
                self.status.grid(row=4, column=1, sticky=E + W, padx=5, ipadx=4)
                self.prev_btn.grid(row=4, column=0, sticky=W, pady=5, padx=10)

        except (KeyError, TclError):
            messagebox.showwarning('Error', 'Please select from the drop down menus, then hit enter!')

        else:
            update_label = Label(self.bot_frame, text="Your videos will open shortly.", bg='gray')
            notice_label = Label(self.bot_frame,
                                 text='*Please note that the "Open All" option may not open all of the videos in '
                                      'the correct order. '
                                      'This is due to varying factors like internet speed and different web browsers.',
                                 bg='gray', wraplength=250)

            update_label.grid(row=5, column=0, sticky=E + W)
            notice_label.grid(row=6, column=0, sticky=E + W)

    def next_vid(self, urls, num):
        new = 0
        current_vid = urls[num]

        webbrowser.open(current_vid, new=new)

        # Need to forget the previous buttons to not mess up new buttons
        self.next_btn.grid_forget()
        self.prev_btn.grid_forget()
        self.status.grid_forget()

        # Create status bar and next/prev buttons
        self.status = Label(self.next_frame, text='Video ' + str(num + 1) + ' of ' + str(len(urls)),
                            relief=SUNKEN, width=16)

        if urls[num] == urls[len(urls) - 1]:
            self.next_btn = Button(self.next_frame, text="Next", state=DISABLED, bg='red', width=8)
        else:
            self.next_btn = Button(self.next_frame, text='Next',
                                   command=lambda: self.next_vid(urls, num + 1), bg='cyan', width=8)

        self.prev_btn = Button(self.next_frame, text='Prev',
                               command=lambda: self.prev_vid(urls, num - 1), bg='pink', width=8)

        self.next_btn.grid(row=4, column=2, sticky=E, pady=5, padx=10)
        self.status.grid(row=4, column=1, sticky=E + W, padx=5, ipadx=4)
        self.prev_btn.grid(row=4, column=0, sticky=W, pady=5, padx=10)

    def prev_vid(self, urls, num):
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

        self.prev_btn.grid(row=4, column=0, sticky=W, padx=10, pady=5)
        self.status.grid(row=4, column=1, sticky=E + W, ipadx=4)
        self.next_btn.grid(row=4, column=2, sticky=E, padx=10, pady=5)

    def vid_opener(self):

        file_in = open('youtube_links.txt', 'r')
        lines = file_in.readlines()

        url_list = []

        for url in lines:  # Adds the youtube links from the file to a list
            url_list.append(url.strip('\n'))

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

        option_list = ['Open all', 'Open when clicked']

        option_btn2 = OptionMenu(self.status_frame, options, *option_list)
        option_btn2.config(width=18, bg='gray', activebackground='gray')
        option_btn2.grid(row=2, column=0, padx=10, pady=10)

        enter_button = Button(self.status_frame, text="Enter",
                              command=lambda: self.get_options(selected, url_list, options),
                              bg='lightgreen', activebackground='lightgreen', width=18)
        enter_button.grid(row=2, column=1, pady=10, padx=10)


# Program starts here
if __name__ == '__main__':
    root = Tk()
    root.title("Random YouTube Video?")  # This is title of program
    root.iconbitmap('C:/Users/white/Desktop/python_work/freecodecamp/feelsdankman_Y7t_icon.ico')
    root.geometry("400x400")
    root.configure(bg='gray')
    root.resizable(False, False)

    # Api key is stored as an environment variable, don't share your api key!
    youtube_key = os.environ.get('YT_KEY')

    youtube_vid = RandomVid(youtube_key)
    root.mainloop()
