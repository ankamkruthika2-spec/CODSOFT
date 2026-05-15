# CODSOFT TASK 1 - TO DO LIST

tasks = []

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            delete_task = int(input("Enter task number to delete: "))

            if 1 <= delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                print(f"'{removed}' deleted successfully!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice. Please try again.")
