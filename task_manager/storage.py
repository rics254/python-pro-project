# task_manager/storage.py

# This module handles reading from and writing to the tasks.txt file

def load_tasks(filename="tasks.txt"):
    """
    Reads tasks from the file and returns them as a list.
    """
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    """
    Writes the task list to the file.
    """
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
