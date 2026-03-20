import sys
from task_manager import add_task, update_task, delete_task, mark_task, list_tasks
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [args]")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            add_task(sys.argv[2])
        elif command == "update":
            update_task(int(sys.argv[2]), sys.argv[3])
        elif command == "delete":
            delete_task(int(sys.argv[2]))
        elif command == "mark-done":
            mark_task(int(sys.argv[2]), "done")
        elif command == "mark-in-progress":
            mark_task(int(sys.argv[2]), "in-progress")
        elif command == "list":
            status_filter = sys.argv[2] if len(sys.argv) > 2 else None
            list_tasks(status_filter)
        else:
            print(f"Unknown command: {command}")
    except IndexError:
        print(f"Missing arguments for command: {command}")
if __name__ == "__main__":
    main()