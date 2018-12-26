import praw
import config
import datetime

items = ['converse', 'vans', 'adidas', 'yeezy', 'pacsun', 'hollister', 'uniqlo']

def reddit_login():
    print("Logging in...")
    r = praw.Reddit(client_id = config.reddit_client_id,
                         client_secret = config.reddit_client_secret,
                         username = config.reddit_username,
                         password = config.reddit_password,
                         user_agent = config.reddit_user_agent)
    print("Login success")
    return r

def get_date(submission):
    return datetime.datetime.fromtimestamp(submission.created)

def compile_deals(r):
    deals = {}
    subreddit1 = r.subreddit('frugalmalefashion')
    hot_python1 = subreddit1.hot(limit = 25)
    for submission in hot_python1:
        if not submission.stickied:
            deals[submission.title] = submission.url
            #print(get_date(submission))
            
    
    subreddit2 = r.subreddit('sneakerdeals')
    hot_python2 = subreddit2.hot(limit = 25)
    for submission in hot_python2:
        if not submission.stickied:
            deals[submission.title] = submission.url
    return deals


def execute_bot(r):
    print("Obtaining comments...")
    for comment in r.subreddit('test').comments(limit=25):
        for item in items:
            if item in comment.body and comment.id not in comments_replied_to:
                print("Matching string found in body...")
                comment.reply("Check https://twitter.com/Mack84471368?lang=en for deals")
                comments_replied_to.append(comment.id)
                print("Replied to comment" + comment.id)

comments_replied_to = []
r = reddit_login()
deals = compile_deals(r)
#execute_bot(r)
        
        
            
