#!/usr/bin/python3
"""This module exports to-do list information for all employees."""

import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get("{}/users".format(url)).json()
    users_id = [user.get("id") for user in users]
    big_data = {}
    for user in users_id:
        response = requests.get("{}/users/{}".format(url, user))
        employee = response.json()

        response2 = requests.get("{}/todos".format(
            url), params={"userId": user})
        todos = response2.json()
        total_tasks = len(todos)

        username = employee.get('username')

        data = {
            user: [
                {"task": todo.get("title"),
                 "completed": todo.get("completed"),
                 "username": username} for todo in todos
                ]
        }
        big_data.update(data)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(big_data, f)
