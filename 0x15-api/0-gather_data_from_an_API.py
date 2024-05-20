#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import urllib.request
import json
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    employee_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com'

    response = urllib.request.urlopen("{}/users/{}".format(url, employee_id))
    employee = json.load(response)
    employee_name = employee.get('name')

    response2 = urllib.request.urlopen("{}/todos".format(url))
    todos = json.load(response2)
    filtered_todos = [todo for todo in todos if todo.get(
        "userId") == employee_id]
    total_tasks = len(filtered_todos)
    completed_tasks = [todo for todo in filtered_todos if todo.get(
        "completed")]
    done_tasks = len(completed_tasks)

    print(
        "Employee {} is done with tasks ({}/{}):".format(employee_name,
                                                         done_tasks,
                                                         total_tasks))
    for i in range(done_tasks):
        print("     {}".format(completed_tasks[i]['title']))
