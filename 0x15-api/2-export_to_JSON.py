#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the CSV format
"""
from sys import argv
import json
import requests


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    req = requests.get(user_url)
    user_data = req.json()

    todo_url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(argv[1]))
    req = requests.get(todo_url)

    todo_data = req.json()

    todo_data = {argv[1]: [
        dict(item, **{'username': user_data["username"]}) for item in todo_data
    ]}

    jsonname = "{}.json".format(argv[1])
    with open(jsonname, 'w') as outfile:
        json.dump(todo_data, outfile)
