import praw
import time

r = praw.reddit(user_agent = "Bot")

words_to_match = ['','','','','']
cache = []

def run_bot():
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit = 25)
    for comment in comments:
        comment_text = comments.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print"Comment found. Comment ID: " + comment.id
            comment.reply('Correction')
            print"replied"
            cache.append(comment.id)
    print"Loop ended"

while True:
    run_bot()
    time.sleep(10)
