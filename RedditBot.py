import praw
import re
import time

reddit = praw.Reddit(clint_id='CAibudbpWHXGRA',
                     client_secret='FzI2wGC9oIFm3bNMB4rYkD1C3dM',
                     user_agent='< by /u/DexyJ>',
                     username='',
                     password='')

print(reddit.read_only)

subreddit = reddit.subreddit("scathach")

for submission in subreddit.hot(limit=10):
    print