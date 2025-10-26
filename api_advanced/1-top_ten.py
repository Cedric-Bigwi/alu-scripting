#!/usr/bin/python3
"""
Module 1-top_ten
Fetches the top 10 hot post titles for a given subreddit using Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALU-Reddit-API-Client/1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check for valid response
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])
    if not data:
        print(None)
        return

    for post in data:
        print(post.get("data", {}).get("title"))
