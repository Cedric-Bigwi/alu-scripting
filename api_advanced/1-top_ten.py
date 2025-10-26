#!/usr/bin/python3
"""Contains the function top_ten
that prints the titles of the first 10 hot posts
listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "ALU-API-advanced:v1.0 (by /u/CedricBigwi)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])
    if not data:
        print(None)
        return

    for post in data:
        print(post.get("data", {}).get("title"))
