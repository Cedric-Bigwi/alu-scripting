#!/usr/bin/python3
"""Contains the recursive function recurse
that returns a list of titles of all hot articles
for a given subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively returns list of all hot post titles.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): Accumulated list of titles.
        after (str): Token for pagination.

    Returns:
        list: Titles of all hot posts, or None if invalid subreddit.
    """
    if hot_list is None:
        hot_list = []

    if not subreddit or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-API-advanced:v1.0 (by /u/CedricBigwi)"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    next_after = data.get("after")
    if next_after:
        return recurse(subreddit, hot_list, next_after)
    return hot_list
