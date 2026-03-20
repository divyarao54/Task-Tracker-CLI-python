from task_store import load_tasks, save_tasks
from datetime import datetime

def add_task(description):
    existing_tasks = load_tasks()
    index = max(int(t["id"]) for t in existing_tasks) + 1 if existing_tasks else 1
    new_task = {
        "id": index,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    existing_tasks.append(new_task)
    save_tasks(existing_tasks)

def update_task(id, description):
    existing_tasks = load_tasks()
    found = False
    for task in existing_tasks:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break
    if not found:
        print(f"Task with id {id} not found.")
        return
    save_tasks(existing_tasks)

def delete_task(id):
    existing_tasks = load_tasks()
    found = False
    for task in existing_tasks:
        if task["id"] == id:
            existing_tasks.remove(task)
            found = True
            break
    if not found:
        print(f"Task with id {id} not found.")
        return
    save_tasks(existing_tasks)

def mark_task(id, status):
    existing_tasks = load_tasks()
    found = False
    for task in existing_tasks:
        if task["id"] == id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break
    if not found:
        print(f"Task with id {id} not found.")
        return
    save_tasks(existing_tasks)

def list_tasks(status=None):
    existing_tasks = load_tasks()

    if not status:
        for task in existing_tasks:
            print(f"{task['id']}. {task['description']} ({task['status']}) - created: {task['createdAt']} - updated: {task['updatedAt']}")

        return
    
    filtered_tasks = [task for task in existing_tasks if task["status"] == status]
    if not filtered_tasks:
        print(f"No tasks found matching status: {status}")
        return
    for task in filtered_tasks:
        print(f"{task['id']}. {task['description']} ({task['status']}) - created: {task['createdAt']} - updated: {task['updatedAt']}")

