#!/usr/bin/python3
"""Contains the function top_ten that prints
the titles of the first 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None
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
