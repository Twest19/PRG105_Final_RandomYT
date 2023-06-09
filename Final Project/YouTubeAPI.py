from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from YouTubeAPIError import *


class YouTubeAPI:
    """This class is responsible for YouTube API request"""
    def __init__(self, api_key):
        # Initialize Api key
        self.api_key = api_key
        self.error = YouTubeAPIError()
        self.response_two = None
        self.vid_list = []

    """Method gathers the categories available on YouTube"""
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

        return my_dict

    """Gathers the links available for a selected category"""
    def link(self, my_dict, click, num):
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

            self.response_two = request.execute()

        except HttpError as e:
            if e.resp.status == 404:
                print(f"A HTTP error occurred: {e}")
                raise NotFoundError()
            else:
                raise APIError(str(e))

        else:
            for item in self.response_two['items']:  # Saves video ids to a list
                self.vid_list.append(f"https://www.youtube.com/watch?v={item['id']}")

            return self.vid_list
