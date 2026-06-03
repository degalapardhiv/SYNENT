tasks = []

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")

while True:
    print("===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.\n")
