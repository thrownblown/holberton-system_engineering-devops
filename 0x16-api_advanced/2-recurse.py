#!/usr/bin/python3
""" queries the Reddit API returns the entire hot list recursivley  """
import requests


def recurse(subreddit, hot_list=[]):
    """ returns the whole hot list  """
    if len(hot_list):
        url = 'https://reddit.com/r/{}/hot.json?after={}'
        url = url.format(subreddit, hot_list.pop(-1))
    else:
        hot_list = []
        url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'holberbot'})
    data = requests.get(url, headers=headers, allow_redirects=True)
    data = data.json().get('data')
    if data.get('after'):
        hot_list += [ch.get('data').get('title')
                     for ch in data.get('children')]
        hot_list.append(data.get('after'))
        return recurse(subreddit, hot_list=hot_list)
    if hot_list:
        return hot_list
    return None
