#!/usr/bin/python3
""" returns the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """function to return the number of subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "PostmanRuntime/7.43.0"}

    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if response.status_code != 200:
            return 0
        return response.json().get("data").get("subscribers")

    except Exception:
        return 0

    