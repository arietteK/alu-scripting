#!/usr/bin/python3
"""Returns a list containing the titles of all hot articles for a given
subreddit using recursive function"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ recursive function """
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    HEADERS = {"User-Agent": "PostmanRuntime/7.43.0"}
    PARAMS = {"after": after, "limit": 100}
    try:
        response = requests.get(URL, headers=HEADERS, params=PARAMS,
                                allow_redirects=False)
        after = response.json().get("data").get("after")
        HOT_POSTS = response.json().get("data").get("children")
        [hot_list.append(post.get('data').get('title')) for post in HOT_POSTS]
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
