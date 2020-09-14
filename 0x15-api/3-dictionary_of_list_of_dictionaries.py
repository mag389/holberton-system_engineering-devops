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

    r_users = requests.get(url + 'users/')

    user_dict = r_users.json()
    retval = {}
    for user in user_dict:
        employee = str(user['id'])
        retval[employee] = []
        task_list = []
        username = user["username"]
        usertasks = requests.get(url + 'todos/' + '?userId=' + employee)
        task_dict = usertasks.json()
        for task in task_dict:
            retval[employee].append({"task": task['title'],
                                     "completed": task['completed'],
                                     "username": username})
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        string = json.dumps(retval)
        f.write(string)
