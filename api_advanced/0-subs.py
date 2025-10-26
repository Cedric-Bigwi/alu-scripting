#!/usr/bin/python3
"""Module for task 0: number_of_subscribers"""
import requests

"""
Returns the number of subscribers for a given subreddit.
If the subreddit is invalid, returns 0.
"""
def number_of_subscribers(subreddit):
    
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ALU-API-advanced:v1.0 (by /u/Cedric-Bigwi)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        return 0
