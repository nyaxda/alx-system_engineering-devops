#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import requests
import pandas as pd
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

    print(
        "Employee {} is done with tasks({}/{}):".format(employee_name,
                                                        len(completed_tasks),
                                                        total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))

    username = employee.get('username')
    data = []
    for todo in todos:
        data.append([employee_id, username, todo.get(
            "completed"), todo.get("title")])

    df = pd.DataFrame(data,
                      columns=["USER_ID", "USERNAME",
                               "TASK_COMPLETED_STATUS",
                               "TASK_TITLE"])
    df.to_csv('{}.csv'.format(employee_id),
              index=False, header=False,
              quotechar='"', quoting=1)
