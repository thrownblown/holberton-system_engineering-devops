#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the CSV format
"""
from sys import argv
import csv
import requests


if __name__ == "__main__":
    if len(argv) != 2:
        print("1-export_to_CSV.py <user_id>")
    else:
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
        req = requests.get(user_url)
        user_data = req.json()

        todo_url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
                    .format(argv[1]))
        req = requests.get(todo_url)
        todo_data = req.json()

        csvname = "{}.csv".format(argv[1])
        with open(csvname, 'w') as csvfile:
            fieldnames = ["userId", "name", "completed", "title"]
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, extrasaction='ignore')
            for task in todo_data:
                task["name"] = user_data.get("username")
                writer.writerow(task)
