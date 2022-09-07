
from sys import argv
from os import remove

def help():
    print('''Usage: 
        todo -a "some task"      addes a task to your list
        todo -d "some task"      delete a task from your list
        todo -l                  lists all of your tasks
        todo -c                  removes everything

          ''')


def write(task):
    with open("/root/.todo.save", "a+") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        f.write(task)
        print("task Added, your new tasks are:\n")
    list_tasks()
    
    
def list_tasks():
    with open("/root/.todo.save", "r") as f:
        for index, task in enumerate(f, start=1):
            print(f"{index}. {task}")


def delete(id):
    with open("/root/.todo.save", "r+") as tasks:
        temp_tasks = tasks.readlines()
        tasks.seek(0) 
        for task in temp_tasks:
            if id not in task:
                tasks.write(task)
        tasks.truncate()
        print("task deleted")
        check_all()
        list_tasks()
        print("your new tasks are:\n")


def check_all():
    with open("/root/.todo.save", "r") as f:
        if len(f.read(100)) == 0:
            print("you don't have tasks, use -a to add your first task")
            exit()


def check_empty_task(task):
    if len(task) == 0:
        print("are you really that stupid? give me something")
        return True
 

def evaluate_task(fun):
    if len(argv) < 3:
        print("you need to give me a task ")
        task = input(": ")
        while check_empty_task(task):
            task = input(": ")
        else:
            if fun == "-a":
                write(task)
            elif fun == "-d":
                delete(task)
        
    else:
        return True
    
def clear():
    ans = input("are you sure you want to delete ? this will delete todo.save from your computer ( no - yes ):  ")
    if ans == "yes":
        remove("/root/.todo.save")
        print("file removed successfully")
    elif ans == "no":
        exit()
    else:
        clear()


def start():
    if len(argv) == 1:
        help()

    elif argv[1] == "-c":
        clear()
    
    elif argv[1] == "-l": 
        check_all()
        list_tasks()
    
    elif argv[1] == "-d":
        if evaluate_task(argv[1]):
            check_all()
            delete(argv[2])
    
    
    elif argv[1] == "-a":
        if evaluate_task(argv[1]):
            write(argv[2])
    else:
        help()


start()
