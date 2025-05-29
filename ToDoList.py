print("welcome to the task manager, what would you like to do.")
tasks= [ ]

while (True):
    print("1. show tasks")
    print("2. remove task")
    print("3. add tasks")
    print("4. exit")
    
    choice = (input ("choose a number(1-4):"))
    
    if choice == "1":
        if not tasks:
            print("no tasks available.")
        else:
            print("your tasks :")
            for i, task in enumerate(tasks , 1):
                print(f"{i}. {tasks}")
                
                
    elif choice == "2":
        if not tasks:
            print("no tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
              print(f"{i}. {tasks}")
              
            try:
                num= int(input("enter task number to remove:"))
                if 1<= num <= len(tasks):
                   removed= tasks.pop(num-1)
                   print(f"tasks removed :{removed}")
            except ValueError:
                print ("enter a valid number.")
                
        
    elif choice == "3":
        task= input("enter your task:")
        tasks.append(task)
        print("task added.")
        
    elif choice == "4":
        print("thank you for using.")
        break
    else:
        print("invalid choice")

        

        
        
        