#!/usr/bin/python3
""" script that uses REST API for a given employee id
    returns info about his/her TODO list progress
"""
import requests
import sys
import urllib


def number_of_subscribers(subreddit):
    """ uses teh reddit api to give the number of subscribers
        in a subreddit
    """
    custom_user = {"User-Agent": "toomanyrequests"}
    url = "http://reddit.com/r/" + subreddit + "/about.json"
    res = requests.get(url, headers=custom_user)
    # print(res.status_code)
    # print(res)
    info = res.json()
    if info.get('error', 'data') == 404:
        return 0
    if type(info) is None:
        return (0)
    # print(info)
    num = info.get("data").get('subscribers', 0)
    return (num)
