import tweepy
import time
import reddit_bot
import config
  
items = {'converse', 'nike', 'vans', 'adidas', 'yeezy', 'pacsun', 'hollister', 'uniqlo', 'patagonia', 'banana', 'levi'}

def twitter_login():
    auth = tweepy.OAuthHandler(config.twitter_consumer_key, config.twitter_consumer_secret)
    auth.set_access_token(config.twitter_access_key, config.twitter_access_secret)
    api = tweepy.API(auth)
    return api

def tweet():
    r = reddit_bot.reddit_login()
    hot_page_titles = reddit_bot.compile_deals(r)
    api = twitter_login()
    for title in hot_page_titles:
        for brand in items:
            if brand in title.lower():
                tweet = title + '\n' + hot_page_titles[title]
                api.update_status(tweet)
                time.sleep(3)
                
def batch_delete(api):
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print ("Deleted:", status.id)
        except:
            print ("Failed to delete:", status.id)   
#batch_delete(twitter_login())
tweet()

