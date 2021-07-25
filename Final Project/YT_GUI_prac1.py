import os
from googleapiclient.discovery import build
from tkinter import *
import webbrowser
import random
import time


root = Tk()
root.title("Random YouTube Video?")  # This is title of program
root.iconbitmap('C:/Users/white/Desktop/python_work/freecodecamp/feelsdankman_Y7t_icon.ico')
root.geometry("330x150")
root.configure(bg='gray')
root.resizable(False, False)

frame = Frame(root)
frame.configure(bg='gray')
frame.grid(row=0, column=0)

api_key = os.environ.get('YT_KEY')


def get_link(my_dict, click, num):
    try:
        result = num.get()
        clicked_label = click.get()
        youtube = build('youtube', 'v3', developerKey=api_key)

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
        pass

    else:
        file = open('youtube_links.txt', 'w')  # This writes the links to a file
        for ids in vid_list:
            vids = f'https://www.youtube.com/watch?v={ids}'  # Inserts the different videos ids into a youtube link
            file.write(vids + '\n')
        file.close()
        vid_opener()


def category():
    youtube = build('youtube', 'v3', developerKey=api_key)
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
    results.set("Results")

    # Create a drop down menu to have user make a selection
    category_drop = OptionMenu(frame, clicked, *my_dict.keys())
    category_drop.config(width=18, bg='gray', activebackground='gray')
    category_drop.grid(row=0, column=0, padx=10, pady=10)

    num_videos = OptionMenu(frame, results, *numbers)
    num_videos.config(width=18, bg='gray', activebackground='gray')
    num_videos.grid(row=1, column=0, padx=10, pady=10)

    enter_button = Button(frame, text="Enter", command=lambda: get_link(my_dict, clicked, results),
                          bg='lightgreen', activebackground='lightgreen', width=18)
    enter_button.grid(row=1, column=1, pady=10, padx=10)


def get_options(select, urls):
    new = 0
    option = select.get()
    if option == 'Randomize':
        random.shuffle(urls)
    elif option == 'Most Popular First':
        urls.reverse()
    elif option == 'Least Popular First':
        pass

    update_label = Label(frame, text="Your videos will open shortly.", bg='gray')
    update_label.grid(row=3, column=0)

    for links in urls:  # Opens the links in a web browser
        webbrowser.open(links, new=new)
        time.sleep(10)


def vid_opener():

    file_in = open('youtube_links.txt', 'r')
    lines = file_in.readlines()

    url_list = []

    for url in lines:  # Adds the youtube links from the file to a list
        url_list.append(url.strip('\n'))

    file_in.close()

    options = ['Randomize', 'Most Popular First', 'Least Popular First']

    selected = StringVar()
    selected.set('Randomize')

    playback_menu = OptionMenu(frame, selected, *options)
    playback_menu.config(width=18, bg='gray', activebackground='gray')
    playback_menu.grid(row=2, column=0, padx=10)

    enter_button = Button(frame, text="Enter", command=lambda: get_options(selected, url_list),
                          bg='lightgreen', activebackground='lightgreen', width=18)
    enter_button.grid(row=2, column=1, pady=10, padx=10)


if __name__ == '__main__':
    category()
    root.mainloop()
