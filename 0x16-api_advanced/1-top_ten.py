#!/usr/bin/python3
""" script that uses REST API for a given employee id
    returns info about his/her TODO list progress
"""
import requests
import sys
import urllib


def top_ten(subreddit):
    """ uses reddit api to give top 10 hot posts
        in a subreddit
    """
    custom_user = {"User-Agent": "toomanyrequests"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    # print(url)
    params = {'limit': 10}
    res = requests.get(url, headers=custom_user, params=params,
                       allow_redirects=False)
    # print(res.status_code)
    if res.status_code != 200:
        print(None)
    else:
        info = res.json()
        for child in info.get('data').get('children'):
            print(child.get('data').get("title"))
