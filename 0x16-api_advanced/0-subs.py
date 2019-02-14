#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers  """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers  """
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'holberbot-subs'})

    data = requests.get(url, headers=headers, allow_redirects=True)
    if data.status_code <= 300:
        data = data.json()
        return data['data']['subscribers']
    return 0
