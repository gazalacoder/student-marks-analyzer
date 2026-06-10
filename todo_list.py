print("Welcome to to-do list app")
tasks = []
while True:
    print("/n1. Add Task")
    print("2. View Task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter choice:")
    if choice == "1":
        task = input("Enter task:")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("/nYour Tasks:")
        for t in tasks:
            print("-",t)
    elif choice == "3":
        print("\nTasks:")
        for i , task in enumerate(tasks):
            print(i, "-", task)
        index = int(input("Enter task number to delete:"))
        tasks.pop(index)
        print("Task Deleted")
    elif choice == "4":
        print("Bye!")
        break
