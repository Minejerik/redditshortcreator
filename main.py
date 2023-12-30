import praw
from getposts import getposts, getcomments, getpostimage, getcommentimage
from getvoices import getcommentvoices, getpostvoices
from utils import clear
from random import randint
from moviepy.video.fx.all import crop
from time import sleep, time
from moviepy.editor import concatenate_videoclips, VideoFileClip, CompositeVideoClip
from colorama import Fore, Back, Style, init
from elevenlabs import generate, play, set_api_key, voices
from keys import ELEVENLABS_API_KEY, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, BACKGROUND_VIDEO

start = time()

api_key = ELEVENLABS_API_KEY

set_api_key(api_key)
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)

clear()
finalposts = []
posts, ids = getposts(reddit, 'askreddit', 3)


for post in posts:
    print("Using post: "+post.title)
    getpostimage(post)
    getpostvoices(post)
    
    post.getClip()
    
    print(Fore.GREEN+"Getting Comments for post: "+post.title+Fore.RESET) 
    comments, ids = getcomments(post, 3)
    for comment in comments:
        getcommentvoices(comment,post.id)
        getcommentimage(comment,post.id)
    post.addComments(comments)
    post.getCommentClip()
    finalposts.append(post)

clips = []

for post in finalposts:
    clips.append(post.clip)
    clips.append(post.commentclip)
    
    
print(Fore.GREEN+"Concatenating clips"+Fore.RESET)

finalclip = concatenate_videoclips(clips, method="compose")


background = VideoFileClip(BACKGROUND_VIDEO).without_audio()

temp = randint(0,int(background.duration-10))

background = background.subclip(temp,temp+finalclip.duration+1)

(w,h) = background.size

crop_width = h * 9/16

x1, x2 = (w - crop_width)//2, (w+crop_width)//2
y1, y2 = 0, h
cropped_background = crop(background, x1=x1, y1=y1, x2=x2, y2=y2)

finalclip = finalclip.resize(width=cropped_background.w)

full = CompositeVideoClip([cropped_background, finalclip.set_pos((0,h/2-finalclip.h/2))])

full.write_videofile("output.mp4", fps=30, threads=8, codec="h264_nvenc")

end = time()

print(Fore.GREEN+"Done! Took "+str(round(end-start,2))+" seconds"+Fore.RESET)