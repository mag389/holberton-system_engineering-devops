#!/usr/bin/python3
""" script that uses REST API for a given employee id
    returns info about his/her TODO list progress
"""
import requests
import sys
import urllib


url = 'https://jsonplaceholder.typicode.com/'
employee = sys.argv[1]

r_user = requests.get(url + 'users/' + employee)
r_task = requests.get(url + 'todos/')

user_dict = r_user.json()
task_dict = r_task.json()
tasks = 0
completed = 0
comp_tasks = []
for task in task_dict:
    # print(type(task))
    # print(type(task['userId']))
    # print(type(employee))
    if task['userId'] == int(employee):
        tasks += 1
        if task['completed'] is True:
            completed += 1
            comp_tasks.append(task)
# print("{}/{}".format(completed, tasks))
# print('-----------------')

line_one = 'Employee {} is done with tasks({}/{}):'.format(
        user_dict['name'], completed, tasks)
print(line_one)
for task in comp_tasks:
    print("	 {}".format(task['title']))
# print(r_user.text)
# print(r_user.json)
