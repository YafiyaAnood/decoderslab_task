
import json
from pathlib import Path

# File used to store tasks permanently
DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load saved tasks from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if isinstance(tasks, list):
            return tasks

        print("Warning: Invalid task data. Starting with an empty list.")
        return []

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save all tasks to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except OSError:
        print("Error: Tasks could not be saved.")
        return False


def add_task(tasks):
    """Add a new task."""
    task_name = input("Enter your task: ").strip()

    if not task_name:
        print("Task name cannot be empty.")
        return

    tasks.append({"name": task_name, "completed": False})

    if save_tasks(tasks):
        print(f"Task added successfully: {task_name}")


def view_tasks(tasks):
    """Display all tasks and their status."""
    print("\n" + "=" * 45)
    print("                 YOUR TO-DO LIST")
    print("=" * 45)

    if not tasks:
        print("No tasks found. Add a task to get started!")
    else:
        for number, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{number}. [{status}] {task['name']}")

    print("=" * 45)


def complete_task(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to complete: "))

        if 1 <= number <= len(tasks):
            task = tasks[number - 1]

            if task["completed"]:
                print("This task is already completed.")
            else:
                task["completed"] = True
                if save_tasks(tasks):
                    print(f"Task completed: {task['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid whole number.")


def delete_task(tasks):
    """Delete a task by its number."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to delete: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)

            if save_tasks(tasks):
                print(f"Task deleted: {removed_task['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    """Run the main application menu."""
    tasks = load_tasks()

    
    print("        PYTHON TO-DO LIST APPLICATION")
    

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List Application!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
