#! usr/bin/env python3
sub = "earthporn"
quantity = 10
import praw
import peekaaa as pk
import pandas as pd
import datetime as dt
import os
from urllib.error import URLError, HTTPError
import urllib.request as web
import shutil
import colorama
from colorama import Fore, Style

reddit = praw.Reddit(client_id='4_449rzO0nHMYg', \
                     client_secret='3W-qwMbWzkIecvoOU9yIuGGRJ-0', \
                     user_agent='wallpaperScraper', \
                     username= pk.username, \
                     password=pk.password)




current_dir = os.getcwd()
dir_path = os.path.join(current_dir, sub)
if not os.path.exists(dir_path):
    os.mkdir(dir_path)


colorama.init(autoreset= True)
subreddit = reddit.subreddit(sub)

print("Downloading Files...")


top_sub = subreddit.top(limit = quantity)

for submission in top_sub:
    fullfilename = os.path.join(dir_path, "{}.jpg".format(submission))
   
    request = web.Request(submission.url, headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    with web.urlopen(request) as response, open(fullfilename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        


    