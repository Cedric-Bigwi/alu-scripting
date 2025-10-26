#!/usr/bin/python3
""" 1-top_ten module prints the titles of the first 10 hot posts """

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALU-Reddit-API-Client/1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
