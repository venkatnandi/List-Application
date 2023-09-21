import json

# Define the file name for saving tasks
TASKS_FILE = "tasks.json"

def add_task():
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    
    task = {
        "task_name": task_name,
        "task_description": task_description,
        "status": "Incomplete",
        "task_id": len(tasks) + 1  # Generate a unique task ID
    }
    
    tasks.append(task)
    print(f"Task '{task_name}' added successfully!")

def list_tasks():
    print("\nTask List:")
    for task in tasks:
        print(f"Task ID: {task['task_id']}")
        print(f"Task Name: {task['task_name']}")
        print(f"Task Description: {task['task_description']}")
        print(f"Status: {task['status']}\n")

def mark_complete():
    task_id = int(input("Enter the task ID to mark as complete: "))
    
    for task in tasks:
        if task['task_id'] == task_id:
            task['status'] = "Complete"
            print(f"Task '{task['task_name']}' marked as complete.")
            break
    else:
        print("Task not found!")

def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    
    for task in tasks:
        if task['task_id'] == task_id:
            tasks.remove(task)
            print(f"Task '{task['task_name']}' deleted successfully.")
            break
    else:
        print("Task not found!")

def save_tasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!")

def load_tasks():
    global tasks
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        tasks = []

# Initialize tasks list
tasks = []

# Load tasks from file when the program starts
load_tasks()

# Update the menu to include the new features
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
