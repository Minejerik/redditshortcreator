from colorama import Fore, Back, Style, init
from selenium.webdriver.support import expected_conditions as EC
from json import load, dump
from selenium import webdriver
import os
from time import sleep
from PIL import Image
from selenium.webdriver.common.by import By
from utils import clear, post as postc, comment as commentc
init(convert=True)


def getposts(reddit, subreddit, limit):
    count = 0
    posts = []
    postids = load(open('data/postids.json', 'r'))
    #gets posts from subreddit
    for post in reddit.subreddit(subreddit).top(time_filter='day'):
        if post.over_18 == False and post.id not in postids:
            count += 1
            post = postc(post.title, post.url, post.id, post.comments)
            posts.append(post)
            postids.append(post.id)
            print(Fore.GREEN+"Added post: "+post.title+Fore.RESET)
            if count >= limit:
                break
        elif post.id in postids:
            print(Fore.YELLOW+"Post already added: "+post.title+Fore.RESET)
        else:
            print(Fore.RED+"Post is NSFW: "+post.title+Fore.RESET)
    print(Fore.LIGHTGREEN_EX+"\nFound "+str(count)+" posts"+Fore.RESET+"\n")
    dump(postids, open('data/postids.json', 'w'))
    return posts, postids

def getcomments(post, limit):
    count = 0
    comments = []
    commentids = load(open('data/commentids.json', 'r'))
    cleanurl = "/".join(post.url.split("/")[:-2])
    #gets comments from post
    for comment in post.comments:
        if len(comment.body) <= 50 and comment.id not in commentids and comment.body != '[removed]' and comment.body != '[deleted]':
            count += 1
            comment = commentc(comment.body, comment.id, cleanurl+"/comment/"+comment.id)
            comments.append(comment)
            commentids.append(comment.id)
            if count >= limit:
                break
    dump(commentids, open('data/commentids.json', 'w'))
    return comments, commentids


def getpostimage(post):
    print(Fore.GREEN+"Getting image for post: "+post.title+Fore.RESET) 
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(post.url)
    sleep(1.5)
    element = driver.find_element(By.ID,f"t3_{post.id}")
    os.makedirs(f"data/images/posts", exist_ok=True)
    element.screenshot(f"data/images/posts/{post.id}.png")
    post.addImagePath(f"data/images/posts/{post.id}.png")
    driver.quit()

def getcommentimage(comment, parentid):
    print(Fore.GREEN+"Getting image for comment"+Fore.RESET) 
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(comment.url)
    sleep(1.5)
    element = driver.find_element(By.ID,"-post-rtjson-content")
    os.makedirs(f"data/images/comments/{parentid}", exist_ok=True)
    element.screenshot(f"data/images/comments/{parentid}/{comment.id}.png")
    comment.addImagePath(f"data/images/comments/{parentid}/{comment.id}.png")
    driver.quit()




# <div class="_1oQyIsiPHYt6nx7VOmd1sz _2rszc84L136gWQrkwH6IaM  Post t3_125z5x9
# getpostimage("125z5x9")