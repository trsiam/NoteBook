# 📝 Mini Project: To-Do List App (Console)

# Write Python code that:

# Shows a menu with options:

# 1. Add task

# 2. View tasks

# 3. Exit

# Keeps asking the user until they choose Exit.

# Stores tasks in a list.

# When the user chooses “View tasks”, it should print all tasks with numbering.
from termcolor import colored
import sys
temp_V=[]
temp_Vtwo=""
u=""
value=0

def add_task():
   global temp_V, temp_Vtwo,u
   print("\n")
   u=str(input("New Task: "))
   temp_V.append(u)
   what_to_do()
   
def task_del():
    global temp_V
    v=int(input("Which task you want to delete->"))
    for i in range(len(temp_V)):
        if i==v-1:
            del temp_V[i]
            break
    what_to_do()

def view_task():
    global temp_V
    print("---------TASKS----------\n")
    for i in range(len(temp_V)):
        print("Task",i+1,"->",temp_V[i])
    what_to_do()

def exit():
    print("Exit")
    sys.exit()

def what_to_do():
    global value
    print("\n")
    print("---------NOTENOOK----------\n")
    print("1. Add task \n2. View tasks \n3. Delete Task \n4. Exit")
    try:      
        value=int(input("What you want to do: "))
    except ValueError:
        print(colored("Invalid input: Please enter a number(1 or 2 or 3)","red"))
        what_to_do()
    print("\n")
    if (value==1):
        add_task()

    if (value==2):
        view_task()

    if (value==3):
        task_del()

    if (value==4):
        exit()


what_to_do()



