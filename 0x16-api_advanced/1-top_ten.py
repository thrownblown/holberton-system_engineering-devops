#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers  """
import requests


def top_ten(subreddit):
    """ returns the number of subscribers  """
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'holberbot'})
    data = requests.get(url, headers=headers, allow_redirects=True).json()
    if len(data['data']):
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
        print('None')
