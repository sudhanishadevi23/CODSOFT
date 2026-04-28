# To-Do List Application
# Author: Your Name
# Description: A simple command-line to-do list manager

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("\nEnter new task: ")
    tasks.append(task)
    print("Task added successfully!")


def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nExiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()