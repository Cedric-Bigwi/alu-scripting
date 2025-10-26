#!/usr/bin/python3
"""Module for task 3: count_words"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursively count occurrences of words in subreddit hot titles"""
    if not word_list or subreddit is None:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALU-API-advanced:v1.0 (by /u/yourusername)'}
    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    # Initialize word counts
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] += title.count(word_lower)

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        # Filter and sort results
        filtered = {k: v for k, v in word_count.items() if v > 0}
        sorted_words = sorted(filtered.items(),
                              key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")

