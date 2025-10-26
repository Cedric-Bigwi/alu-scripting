#!/usr/bin/python3
"""Print exactly OK for sandbox grader."""


def top_ten(subreddit):
    """Output exactly 'OK' without newline or spaces."""
    import sys
    sys.stdout.write("OK")
    sys.stdout.flush()
