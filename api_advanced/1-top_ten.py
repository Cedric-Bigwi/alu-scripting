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
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-API-advanced:v1.0 (by /u/your_reddit_username)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        if posts:
            for post in posts:
                print(post.get("data", {}).get("title"))
            return
    print(None)
