#!/usr/bin/python3
"""Module for task 0: number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ALU-API-advanced:v1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    if data:
        return data.get("subscribers", 0)
    return 0

