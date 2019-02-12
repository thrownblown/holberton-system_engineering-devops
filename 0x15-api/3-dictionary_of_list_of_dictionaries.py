#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the CSV format
"""
import json
import requests

if __name__ == "__main__":
    final_data = {}
    user_url = "https://jsonplaceholder.typicode.com/users/"
    req = requests.get(user_url)
    user_data = req.json()
    for user in user_data:
        todo_url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
                    .format(user["id"]))
        req = requests.get(todo_url)

        todo_data = req.json()

        final_data[user["id"]] = [
            dict(item, **{'username': user["username"]}) for item in todo_data
        ]

    jsonname = "todo_all_employees.json"
    with open(jsonname, 'w') as outfile:
        json.dump(final_data, outfile)
