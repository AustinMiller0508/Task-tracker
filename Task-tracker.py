#Austin Miller
#Task Tracker - track, manage, and add tasks to track life's to-dos

#Functionality:
#   Due Date
#   Day at a glance
#   Week at a glance
#   Add
#   Statuses (To-Do, In Progress, Complete)
#   Last 10 accomplishments
#   Drop

import time


class Task:
    def __init__(self):
        self.dueDate = 0
        self.status = "To Do"
        self.name = ""
        self.description = ""
        
def main_menu():
    programExit = False
    
    while(programExit == False):
        print("          Menu          \n------------------------\n1)    Today at a glance\n2)    Week at a glance\n3)    New task\n4)    Update task\n5)    View task\n6)    Last 10 Accomplishments\n7)    Quit\n-----------------------\n\nPlease select the desired action:")
        selected = input()
        if(selected == "1"):
            print("Nioce")
        if(selected == "7"):
            print("See you again soon!")
            programExit = True

def main():
    
    main_menu()

    return 0

main()
