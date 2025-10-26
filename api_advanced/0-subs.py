#!/usr/bin/python3
"""This module defines a function that returns
the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-API-advanced:v1.0 (by /u/CedricBigwi)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Reddit returns 302 redirect for invalid subreddits
    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        if not isinstance(subscribers, int):
            return 0
        return subscribers
    except Exception:
        return 0
