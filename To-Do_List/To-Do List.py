filename = "tasks.txt"

def add_task():
    task = input("Enter a new task: ")
    with open(filename, "a") as file:
        file.write(task + " | Pending\n")
    print("Task added.\n")

def view_tasks():
    print("\nYour To-Do List:")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No tasks yet.")
            else:
                for i, line in enumerate(lines, start=1):
                    print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No task file found yet.")

def mark_done():
    view_tasks()
    number = int(input("\nEnter the task number to mark as done: "))
    with open(filename, "r") as file:
        tasks = file.readlines()
    task_parts = tasks[number - 1].split(" | ")
    task_parts[1] = "Done\n"
    tasks[number - 1] = " | ".join(task_parts)
    with open(filename, "w") as file:
        file.writelines(tasks)
    print("Task marked as done.\n")

def delete_task():
    view_tasks()
    number = int(input("\nEnter the task number to delete: "))
    with open(filename, "r") as file:
        tasks = file.readlines()
    deleted = tasks.pop(number - 1)
    with open(filename, "w") as file:
        file.writelines(tasks)
    print("Deleted:", deleted.strip())

def menu():
    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option.")

menu()