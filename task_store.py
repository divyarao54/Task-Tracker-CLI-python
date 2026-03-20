import os
import json

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json", mode="r", encoding="utf-8") as read_file:
        try:
            tasks_data = json.load(read_file)
        except json.JSONDecodeError as e:
            print("Error reading task... ", e.msg)
            return []
    return tasks_data

def save_tasks(tasks):
    with open("tasks.json", mode="w", encoding="utf-8") as write_file:
        json.dump(tasks, write_file, indent=2)