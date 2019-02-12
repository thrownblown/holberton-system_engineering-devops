#!/usr/bin/python3
"""
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) != 2:
        print("0-gather_data_from_an_API.py <user_id>")
    else:
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
        req = requests.get(user_url)
        user_data = req.json()

        print("Employee {} ".format(user_data.get("name")), end="")

        done_todo = (
            "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
            .format(argv[1]))
        todo_url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
                    .format(argv[1]))
        req = requests.get(done_todo)
        complete_todo_data = req.json()

        print("is done with tasks({}".format(len(complete_todo_data)), end="")

        req = requests.get(todo_url)
        todo_data = req.json()

        print("/{}):".format(len(todo_data)))

        for task in complete_todo_data:
            print("\t {}".format(task.get("title")))
            pprint.pprint(task)
