TASK_FILE = "task.txt"

def load_task():
    try:
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Remove Tasks")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty")
    else:
        print("\nYour Tasks")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"task '{task}' added successfully.")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return 
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"task '{removed}' removed successfully")
        else: print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def main():
    tasks = load_task()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exitig To-Do List.")
            break
        else:
            print("Invalid input. Please try again.")

main()

