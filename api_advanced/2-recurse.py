#!/usr/bin/python3
"""Module for task 2: recurse"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns list of all hot post titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALU-API-advanced:v1.0 (by /u/yourusername)'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

