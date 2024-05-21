#!/usr/bin/python3
"""
This module exports to-do list information for a given employee ID.

It fetches the employee and their tasks from a given URL and
exports the data in CSV format.
"""
# Using what you did in the task #0,
# extend your Python script to export data in the  format.

#   Records all tasks that are owned by this employee
#   Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
#   File name must be: USER_ID.csv

import requests
import pandas
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Not Found")
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com'

    response = requests.get("{}/users/{}".format(url, employee_id))
    employee = response.json()
    employee_name = employee.get('name')

    response2 = requests.get("{}/todos".format(
        url), params={"userId": sys.argv[1]})
    todos = response2.json()
    total_tasks = len(todos)
    completed_tasks = [todo.get("title") for todo in todos if todo.get(
        "completed")]

    username = employee.get('username')
    data = []
    for todo in todos:
        data.append([employee_id, username, todo.get(
            "completed"), todo.get("title")])

    df = pandas.DataFrame(data, columns=["USER_ID", "USERNAME",
                                         "TASK_COMPLETED_STATUS",
                                         "TASK_TITLE"])
    df.to_csv('{}.csv'.format(employee_id),
              index=False, header=False,
              quotechar='"', quoting=1)
