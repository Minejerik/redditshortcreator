import os
from utils import cleantext
from elevenlabs import generate, play, set_api_key, voices, save
from keys import ELEVENLABS_VOICE


def getcommentvoices(comment, parentid):
    
    
    audio = generate(
        text=cleantext(comment.body),
        voice=ELEVENLABS_VOICE,
        model="eleven_multilingual_v2"
    )
    
    os.makedirs(f"data/voices/comments/{parentid}", exist_ok=True)
    save(audio, f"data/voices/comments/{parentid}/{comment.id}.mp3") 
    comment.addVoicePath(f"data/voices/comments/{parentid}/{comment.id}.mp3")
    return f"data/voices/comments/{parentid}/{comment.id}.mp3"

def getpostvoices(post):
    
    
    audio = generate(
        text=cleantext(post.title),
        voice=ELEVENLABS_VOICE,
        model="eleven_multilingual_v2"
    )
    
    os.makedirs(f"data/voices/posts", exist_ok=True)
    save(audio, f"data/voices/posts/{post.id}.mp3")
    post.addVoicePath(f"data/voices/posts/{post.id}.mp3")
    return f"data/voices/posts/{post.id}.mp3"