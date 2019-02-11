#!/usr/bin/python3
""" prepares data for easier viewing """
import requests
from sys import argv
"""
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list
progress in this exact format:
First line:
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
and non-completed tasks. Second and N next lines display the title of
completed tasks: Tab TASK_TITLE (with 1 tabulation + 1 space before
"""

# import pdb; pdb.set_trace()
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
req = requests.get(user_url)
user_data = req.json()
print("Employee {} ".format(user_data['name']), end="")

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
    print("\t {}".format(task["title"]))
