#!/usr/bin/python3
""" script that uses REST API for a given employee id
    returns info about his/her TODO list progress
"""
import csv
import requests
import sys
import urllib


url = 'https://jsonplaceholder.typicode.com/'
employee = sys.argv[1]

r_user = requests.get(url + 'users/' + employee)
r_task = requests.get(url + 'todos/')

user_dict = r_user.json()
task_dict = r_task.json()

name = user_dict['name']
filename = employee + '.csv'
with open(filename, 'w+', newline='') as csvfile:
    linewriter = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
    for task in task_dict:
        if task['userId'] == int(employee):
            linewriter.writerow([employee, name,
                                task['completed'], task['title']])
