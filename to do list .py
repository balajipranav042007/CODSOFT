tasks=[]
while True:
    print("LIST:")
    print("1 - View tasks")
    print("2 - Add task")
    print("3 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks")
        else:
            for i in range(len(tasks)):
                print(str(i + 1) + ". " + tasks[i])

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
