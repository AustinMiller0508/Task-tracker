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
noVariations = ["no","none","n/a","nah","nope"]
tasks = []


class Task:
    def __init__(self):
        self.dueDate = time.time()
        self.status = "To Do"
        self.name = ""
        self.description = ""
        
def savedTaskInit():
    name = ""
    description = ""
    date = ""
    try:
        with open("tasks.csv") as taskFile: #open save file to reinitialize each task at startup
            for line in taskFile:
                i = 0
                commacount = 0
                while (i < len(line)):
                    if (line[i] == ','): #increment the current position being read
                        commacount += 1
                    elif (commacount == 0): # get task name from file
                        name += line[i]
                    elif (commacount == 1): # get description from file
                        descrtiption += line[i]
                    elif (commacount == 2): #get due date from file
                        date += line[i]
                    i += 1
                initTask(date,name,description) #pass read data from file to init function

def removeFromSave(pos):
    tasksOverwrite = ""
    with open("tasks.csv") as taskFile:
        i = 0
        for line in taskFile:
            if(i != pos): #rewrite all lines except the position specified
                tasksOverwrite += line
            i += 1
    taskFile.close()
    f = open("tasks.csv", "w") #write over save file with new data
    f.write(tasksOverwrite)
    f.close()
    return

def saveTask(task,pos):
    tasksOverwrite = ""
    with open("tasks.csv") as taskFile:
        i = 0
        for line in taskFile:
            if(i != pos): #rewrite all lines except the position specified
                tasksOverwrite += line
            else:
                tasksOverwrite += task.name + "," + task.description + "," + task.status + "," + task.dueDate + "\n"
            i += 1
    taskFile.close()
    f = open("tasks.csv", "w") #write over save file with new data
    f.write(tasksOverwrite)
    f.close()
    return

def saveTask(task): #override function for saving newly added tasks
    f = open("tasks.csv", "a") #append new task to end of file
    f.write(task.name + "," + task.description + "," + task.status + "," + task.dueDate + "\n")
    f.close()
    return
                


def initTask(date,name,description):
    
    curTask = Task()                                #create new task and add to list of tasks
    tasks.append(curTask)
    curTask.name = name                             #Set task values based on file data
    curTask.description = description
    curTask.dueDate = date
    
    return
                

def mainMenu():
    programExit = False
    
    while(programExit == False):
        print("          Menu          \n------------------------\n1)    Today at a glance\n2)    Week at a glance\n3)    New task\n4)    Update task\n5)    View tasks\n6)    Last 10 Accomplishments\n7)    Quit\n-----------------------\n\nPlease select the desired action:")
        selected = input()
        if(selected == "3"):                        #if menu option 3 is chosen run the create task function
            createTask()
        if(selected == "7"):
            print("See you again soon!")
            programExit = True

def createTask():
    validDate = False
    
    curTask = Task()                                #create new task and add to list of tasks
    tasks.append(curTask)
    print("\nWhat would you like this task to be named?\n")
    name = input()                                  #gather task name
    print("\nPlease add a description for the task.\n")
    description = input()                           #gather task description
    print("\nWhen is this task due? Please use the mm/dd/yyyy format")
    while (validDate == False):
        date = input()
        try:
            realDate = time.strptime(date, "%m/%d/%Y")  #convert user input to time for later comparison
            validDate = True
        except:
            print("\nThe date you entered is invalid, please try again...\n")

    curTask.name = name                             #Set task values based on user input
    curTask.description = description
    curTask.dueDate = realDate

    print("\nTask created successfully!\n")
    return

def main():

    savedTasksInit()
    mainMenu()

    return 0

main()
