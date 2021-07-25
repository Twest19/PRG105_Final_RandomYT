import webbrowser
import random


def vid_opener():
    new = 0

    file_in = open('youtube_links.txt', 'r')
    lines = file_in.readlines()

    url_list = []

    for url in lines:  # Adds the youtube links from the file to a list
        url_list.append(url.strip('\n'))

    file_in.close()

    print("\nVideo Options:"
          "\nRandomize"
          "\nOne to ten"
          "\nTen to one")

    #  Allows user to choose video playback order
    choice = str(input("How would you like the videos to be played (R, OTT, TTO? ")).upper()
    if choice == 'R':
        random.shuffle(url_list)
    elif choice == 'TTO':
        url_list.reverse()
    elif choice == 'OTT':
        pass

    for links in url_list:  # Opens the links in a web browser
        webbrowser.open(links, new=new)

    print("Enjoy!")


if __name__ == '__main__':
    vid_opener()
