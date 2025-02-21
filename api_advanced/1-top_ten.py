#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """titles of the first 10 hot posts listed for a given subreddit"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    HEADERS = {"User-Agent": "PostmanRuntime/7.43.0"}
    try:
        response = requests.get(URL, headers=HEADERS, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            HOT_POSTS = data.get("data", {}).get("children", [])

            for post in HOT_POSTS[:10]:
                print(post.get('data', {}).get('title'))
            else:
                print(None)
    except Exception:
        print(None)
