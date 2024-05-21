#!/usr/bin/python3
"""This module exports to-do list information for a given employee ID."""

import json
import requests
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

    data = {
        employee_id: [
            {"task": todo.get("title"),
             "completed": todo.get("completed"),
             "username": username} for todo in todos
             ]
    }

    with open('{}.json'.format(employee_id), 'w') as f:
        json.dump(data, f)
