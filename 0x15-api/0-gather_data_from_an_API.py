#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    employee_id = int(sys.argv[1])
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
    done_tasks = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(employee_name,
                                                        done_tasks,
                                                        total_tasks))
    for i in range(done_tasks):
        print("\t {}".format(completed_tasks[i]))
