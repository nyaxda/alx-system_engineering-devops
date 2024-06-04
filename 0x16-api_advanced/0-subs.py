#!/usr/bin/python3
"""
Query the Reddit API and return the number of
subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of
    subscribers for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/124.0.0.0 Safari/537.36'
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
