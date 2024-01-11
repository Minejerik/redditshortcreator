# Reddit Shorts Sreator
creates youtube shorts using elevenlabs and reddit api     
### BE WARNED MOST OF THIS CODE WAS WRITTEN OVER A YEAR AGO!! SO MOST OF IT IS GARBAGE!!
## Setup

First clone the repo with git

`git clone https://github.com/Minejerik/redditshortcreator`

Then install dependancies

`pip install moviepy praw elevenlabs colorama translators`

Next download a background video and change the `BACKGROUND_VIDEO` variable in `keys.py` to the path to your video

Then get elevenlabs api key [here](https://elevenlabs.io/?from=partnermills8504) (I get a small commission if you use this link) and change the `ELEVENLABS_API_KEY` variable in `keys.py` to your api key

Create an app with reddit and change the `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` in `keys.py` to what you get from reddit

run `python main.py` on windows or `python3 main.py` on linux/mac

## Customization

you do not need to use minecraft as the background, you can use anything.   
also if you don't like the default voice `Antoni` you can change in to any premade voice or any cloned voice, just change the `ELEVENLABS_VOICE` variable in `keys.py` to the name of your new voice.   

you can also change if the audio that is spoken is translated or not, and the the translation engine being used. look in `keys.py` to change this stuff.
