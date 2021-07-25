import os
from googleapiclient.discovery import build
from tkinter import *


api_key = os.environ.get('YT_KEY')


def main(key):
    youtube = build('youtube', 'v3', developerKey=key)
    request = youtube.videoCategories().list(
        part='snippet',
        regionCode='US'
    )

    response_one = request.execute()  # Execute the youtube api request for categories
    my_dict = {}
    for item in response_one['items']:  # This takes the vid category numbers from youtube and puts them in a dictionary
        if item['snippet']['assignable'] is False:
            pass
        else:
            tube_dict1 = item['snippet']['title']
            tube_dict2 = item['id']
            my_dict[tube_dict1] = tube_dict2

    my_dict['Trending'] = '0'

    print(f"{'='*10} Here are the categories! {'='*10}")
    for k in my_dict.keys():
        print(k)

    video_saver(key, my_dict)


def video_saver(key, my_dict):
    category = str(input("\nPlease select a category: ")).title()  # Gets category from user
    results = int(input("\nHow many videos would you like to see (number 1 - 40): "))

    youtube = build('youtube', 'v3', developerKey=key)

    request = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        chart='mostPopular',
        regionCode='US',
        videoCategoryId=my_dict[category],
        maxResults=results
    )
    # Uses selected category to get video ids from

    vid_list = []

    response_two = request.execute()

    for item in response_two['items']:  # Saves video ids to a list
        vid_list.append(item['id'])

    file = open('youtube_links.txt', 'w')  # This writes the links to a file
    for ids in vid_list:
        vids = f'https://www.youtube.com/watch?v={ids}'  # Inserts the different videos ids into a youtube link
        file.write(vids + '\n')
    file.close()


if __name__ == '__main__':
    main(api_key)
