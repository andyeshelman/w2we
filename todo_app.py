def help():
    print("Options:",
       "(add) to add a task",
       "(view) to view tasks",
       "(complete) to mark a task as complete",
       "(delete) to delete a task",
       "(quit) to quit",
       "(help) for help", sep = "\n")

def add_task(tasks):
    task = input("Enter task: ").lower()
    if task in tasks[0]:
        print(f"'{task}' is already an active task.")
    elif task in tasks[1]:
        print(f"'{task}' is already a completed task.")
    else:
        tasks[0].append(task)

def view_tasks(tasks):
    print("Active Tasks:")
    for task in tasks[0]:
        print("\t"+task)
    print("Completed Tasks:")
    for task in tasks[1]:
        print("\t"+task)

def complete_task(tasks):
    task = input("Enter task to mark as complete: ").lower()
    try:
        tasks[0].remove(task)
        tasks[1].append(task)
    except:
        print(f"'{task}' is not an active task.")

def delete_task(tasks):
    task = input("Enter task to delete: ").lower()
    try:
        tasks[0].remove(task)
    except:
        try:
            tasks[1].remove(task)
        except:
            print(f"'{task}' is neither an active nor completed task.")

print("Welcome to ToDo list app!")

help()

# task_list[0] is list of active tasks
# task_list[1] is list of completed tasks
task_list = ([],[])

while True:

    option = input("Enter option: ").lower()

    if option == "add":
        add_task(task_list)
    elif option == "view":
        view_tasks(task_list)
    elif option == "complete":
        complete_task(task_list)
    elif option == "delete":
        delete_task(task_list)
    elif option == "quit":
        break
    elif option == "help":
        help()
    else:
        print("Command unrecognized")