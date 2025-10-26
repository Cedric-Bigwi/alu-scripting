#!/usr/bin/python3
"""Contains the recursive function count_words
that counts occurrences of keywords in the titles
of all hot articles for a given subreddit."""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Recursively count occurrences of words in subreddit hot titles.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count.
        after (str): Token for pagination.
        word_count (dict): Accumulator for word counts.

    Returns:
        None: Prints sorted results or nothing for invalid subreddit.
    """
    if word_count is None:
        word_count = {}

    if not subreddit or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-API-advanced:v1.0 (by /u/CedricBigwi)"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            word_count[w] = word_count.get(w, 0) + title.count(w)

    next_after = data.get("after")
    if next_after:
        return count_words(subreddit, word_list, next_after, word_count)

    sorted_counts = sorted(
        [(k, v) for k, v in word_count.items() if v > 0],
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_counts:
        print("{}: {}".format(word, count))
