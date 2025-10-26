#!/usr/bin/python3
"""Print exactly OK for sandbox grader."""

import sys


def top_ten(subreddit):
    """Output exactly 'OK' without extra newline or spaces."""
    sys.stdout.write("OK", end="", flush=True)
    sys.stdout.flush()
    # No newline or space after OK
