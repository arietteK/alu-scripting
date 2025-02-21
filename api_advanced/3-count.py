#!/usr/bin/python3
"""Recursive function that parses the title of all hot articles, and prints a
sorted count of given keywords."""

import requests


def count_words(subreddit, word_list=None, hot_list=[], after=""):
    if word_list is None:
        word_list = []
    """Recursive function"""
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
            return count_words(subreddit, word_list, hot_list, after)

        new_dict = {}
        word_list = set([wrd.lower() for wrd in word_list])
        for title in hot_list:
            for word in title.split():
                if word.lower() in new_dict:
                    new_dict[word.lower()] += 1
                else:
                    new_dict.update({word.lower(): 1})

        sorted_dict = sorted(new_dict.items(), key=lambda x: (-x[1], x[0]))
        for key, value in sorted_dict:
            if (key in word_list) and (value > 0):
                print("{}: {}".format(key, value))
    except Exception:
        return None
