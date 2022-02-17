#!/usr/bin/python3
"""Query Reddit API for numbers of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
return number of subscribers for a given subredit
return 0 if invalid subreddit is given
"""
    url = "https://www.reddit.com/r/{}/about.json"/format(subreddit)

    headers=request.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    res = request.get(url, headers=headers).json()
    subscribers = res.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
