
# MCC - PRG105 Final Project - *UPDATED* 5/25/23

## FAQ

### What does it do?
Uses a tkinter GUI to get a users preferences on the random YouTube videos they want to see. It then uses those
preferences to pull the correct videos from the YouTube API. The videos are then opened in the users default
browser or in a local VLC Media Player.

### What does it NOT do?
The videos are not necessarily random, rather they are pulled from the most popular videos in each category for the day. 
This could be modified to add more randomness in the video selection by gathering more videos from a category and selecting a few from that. 
You could also make it so the category is not selectable to another added element of surprise.

### How to use it?
A simple graphical user interface window will appear. At the top of the window you will see a text label that
asks you to choose a video category and the number of videos you want to see. The categories are inside a drop
down menu, as are the number of videos. The number of videos option is just giving you the option to play
anywhere from 1 - 15 videos. Later on you will be able to select if you want the videos to open all at once,
open via a next button, or open in a local video player. Hit enter to submit your choices, if you do not the program will go no
further. Also if you hit enter without making a choice in one of the boxes, it will pop up a message window
telling you to make a selection.

After you have hit enter a new set of drop down menus will appear. These menus will give you the option of how
you want the videos to appear. The first box that says "Randomize" has several options for what order the
videos should play in. "Randomize" will randomize the order, "Most Popular First" will play the most popular
video first, and "Least Popular First" will play the least most popular video first. The "Options" menu gives
you the choice of "Open All" which will open all the videos at once in your browser. "Open on Click" which
will open the first video automatically and then consecutive videos will be opened by clicking the next button
or previous buttons. "Play Locally" is the last option and opens a local media player window that lets you control various media player commands, as well as changing of the video.

Your video(s) should now have been opened in your default web browser or locally for your viewing pleasure.


## Requirements for use

```bash
    pip install --upgrade google-api-python-client
    pip install tk
```

You will also NEED to get your own YouTube API key. Without it the program will not work! It is completely
    free, you just need to create a Google account. DO NOT SHARE YOUR API KEY! I have put mine in an environment
    variable so that others can not access it. I would recommend you do so as well! There is also a limit per day
    on the number of requests you can send to the YouTube API. The limit for free accounts is 10,000 quota a day.
    This program only uses about 2-3 quota per use, so you should never hit that limit.

You can find out more about this here: 
- https://developers.google.com/youtube/v3/getting-started
- https://developers.google.com/youtube/v3/quickstart/python

I would also like to recommend that you have a YouTube account. YouTube sometimes has age restrictions on
    videos, thus requiring a YouTube account.
    
## Resources that helped me get started:

#### YouTube API links/Resources:
- https://developers.google.com/youtube
- https://developers.google.com/youtube/v3/getting-started
- https://developers.google.com/youtube/v3/quickstart/python
- https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md
- https://github.com/googleapis/google-api-python-client/blob/master/docs/README.md
- https://github.com/youtube/api-samples
- https://github.com/youtube/api-samples/blob/master/python/README.md

#### Corey Schafer YouTube:
 - [Corey Schafer: Python YouTube API Tutorial: Getting Started](https://www.youtube.com/watch?v=th5_9woFJmk&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=3)
 - [Corey Schafer: Python YouTube API Tutorial: Calculating the Duration of a Playlist](https://www.youtube.com/watch?v=coZbOM6E47I&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&index=3)
#### Tkinter GUI Resources:
 - [freecodecamp.org Tkinter course](https://youtu.be/YXPyB4XeYLA)
#### Python Resources:
 - [Webbrowser Python Resources:](https://docs.python.org/3/library/webbrowser.html)

 - [Python Random](https://docs.python.org/3/library/random.html)
 
 - [Python OS](https://docs.python.org/3/library/os.html)
 
