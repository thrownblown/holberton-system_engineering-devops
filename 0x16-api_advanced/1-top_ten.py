#!/usr/bin/python3
""" queries the Reddit API and 10 top posts  """
import requests
from json.decoder import JSONDecodeError


def top_ten(subreddit):
    """ returns the number of subscribers  """
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'holberbot'})
    try:
        data = requests.get(url, headers=headers, allow_redirects=False).json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    except KeyError:
        print('None')
    except JSONDecodeError:
        print('None')
