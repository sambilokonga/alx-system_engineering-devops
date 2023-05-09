#!/usr/bin/python3
""" This script queries the Reddit API and returns the number of subscribers
    of the passed in subreddit """
import requests


def number_of_subscribers(subreddit):
    try:
        subscribers = requests.get('https://www.reddit.com/r/{}/about.json'.
                                   format(subreddit), allow_redirects=False,
                                   headers={'User-Agent': 'custom'})
        return subscribers.json().get('data').get('subscribers')
    except:
        return 0
