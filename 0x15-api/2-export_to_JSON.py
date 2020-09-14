#!/usr/bin/python3
""" script that uses REST API for a given employee id
    returns info about his/her TODO list progress
"""
import json
import requests
import sys
import urllib

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee = sys.argv[1]

    r_user = requests.get(url + 'users/' + employee)
    r_task = requests.get(url + 'todos/' + '?userId=' + employee)

    user_dict = r_user.json()
    task_dict = r_task.json()
    # print(type(task_dict))
    # print(task_dict)
    retval = {"2": []}
    task_list = []
    username = user_dict["username"]
    for task in task_dict:
        retval['2'].append({"task": task['title'],
                            "completed": task['completed'],
                            "username": username})
    filename = employee + '.json'
    with open(filename, 'w+') as f:
        string = json.dumps(retval)
        f.write(string)
