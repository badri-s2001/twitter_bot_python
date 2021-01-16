from time import time
import tweepy

auth = tweepy.OAuthHandler('mHSizfML3OHeYQWlzFZJohPEq', 'fc2GIITPr1fUN3XyIjIKBJerSp7jK26VmjB02KDxuHDZ5A3o6n')
auth.set_access_token('785337927685378048-lg6yhgW6JMxOqkJ91wwJLFMGxGucNqz', '31PIkTwYZE6FUnjiwLaPCtAYaVfCcMovWne1ILo6jjcdv')

api = tweepy.API(auth)


# for follower in tweepy.Cursor(api.followers).items():
#     if follower.name == 'Goku_Technocrat':
#         follower.follow()
#         break


search_string = 'Messi'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

