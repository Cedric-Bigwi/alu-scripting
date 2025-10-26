#!/usr/bin/python3
"""
1-top_ten module

This module contains a single function, `top_ten`, which queries the Reddit API
to retrieve and display the titles of the top 10 hot posts from a given subreddit.

Usage:
    >>> top_ten("python")
    (Prints the titles of the first 10 hot posts on the 'python' subreddit)

If the subreddit is invalid or cannot be accessed, the function prints None.

Example:
    $ python3 1-main.py programming
    Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
    How a 64k intro is made
    HTTPS on Stack Overflow: The End of a Long Road
    ...

Requirements:
    - Must use the `requests` module
    - Must not follow redirects (use `allow_redirects=False`)
    - Must handle invalid subreddit names gracefully
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles directly to stdout.
               If the subreddit is invalid, prints None.
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
