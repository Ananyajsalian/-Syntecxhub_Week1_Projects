"""
To-Do List Manager
Syntecxhub Week 1 - Project 3
Author: Ananya
Description: CRUD application with JSON file persistence for tasks.
"""

import json
import os

FILE_NAME = "tasks.json"

def load_tasks() -> list:
    """Load tasks from JSON file. Return empty list if file not found."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks: list) -> None:
    """Save the current task list to JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks: list) -> None:
    """Add a new task to the list."""
    task_desc = input("Enter new task: ").strip()
    if task_desc:
        tasks.append({"task": task_desc, "done": False})
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("Task cannot be empty.")

def view_tasks(tasks: list) -> None:
    """Display all tasks with their completion status."""
    if not tasks:
        print("📝 No tasks in your list yet.")
        return
    print("\n--- Your Tasks ---")
    for index, item in enumerate(tasks, 1):
        status = "✓ Done" if item["done"] else "○ Pending"
        print(f"{index}. [{status}] {item['task']}")

def delete_task(tasks: list) -> None:
    """Delete a task by its number."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(task_num)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid task number.")

def mark_done(tasks: list) -> None:
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark done: ")) - 1
        tasks[task_num]["done"] = True
        save_tasks(tasks)
        print("✅ Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main() -> None:
    """Run the main menu loop for the To-Do List app."""
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1': add_task(tasks)
        elif choice == '2': view_tasks(tasks)
        elif choice == '3': delete_task(tasks)
        elif choice == '4': mark_done(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else: print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
