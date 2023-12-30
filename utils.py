from os import system, name
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


words =[
    "shitty",
    "fuck"
]

cleanwords = [
    "crappy",
    "frick"
]

class post:
    def __init__(self, title, url, id, comments):
        self.title = title
        self.url = url
        self.id = id
        self.comments = comments
        self.commentList = []
        self.voicePath = None
        self.imagePath = None
        self.clip = None
        self.commentclip = None
    
    def addImagePath(self, path):
        self.imagePath = path

    def addVoicePath(self, path):
        self.voicePath = path

    def addComments(self, comments):
        self.commentList = comments
        
    def getClip(self):
        audio = AudioFileClip(self.voicePath)
        image = ImageClip(self.imagePath).set_duration(audio.duration).set_audio(audio)
        self.clip = image
    
    def getCommentClip(self):
        clips = []
        for c in self.commentList:
            clips.append(c.getClip())
        final = concatenate_videoclips(clips)
        self.commentclip = final


class comment:
    def __init__(self, body, id, url):
        self.body = body
        self.id = id
        self.voicePath = None
        self.url = url
        self.imagePath = None
        self.clip = None
    
    def addVoicePath(self, path):
        self.voicePath = path

    def addImagePath(self,path):
        self.imagePath=path
        
    def getClip(self):
        audio = AudioFileClip(self.voicePath)
        image = ImageClip(self.imagePath).set_duration(audio.duration).set_audio(audio).resize(width=395)
        self.clip = image
        return image
        
    


def cleantext(text):
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    for i in range(0, len(text.split())):
        temp = text.split()[i]
        if temp.startswith("http"):
            text = text.replace(temp, "")
        if "no." in temp:
            text = text.replace(temp, "no .")
    for i in range(0, len(words)):
        text = text.replace(words[i], cleanwords[i])
    
    return text

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')