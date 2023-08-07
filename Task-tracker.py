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
import os
tasks = []


#----------------------------Task-Funcs--------------------------------#

class Task:
    def __init__(self):
        self.dueDate = ""
        self.status = "To Do"
        self.name = ""
        self.description = ""

def setDescription(task):
    print("\nPlease add a description for the task.\n")
    description = input()                           #gather task description
    task.description = description

def setName(task):
    print("\nWhat would you like this task to be named?\n") #gather task name
    name = input()
    task.name = name

def setStatus(task):
    print("\nWhat is the status of this task?\n") #gather task status (will standardize this later with selection banks)
    status = input()
    task.status = status

def setDate(task):
    validDate = False
    print("\nWhen is this task due? Please use the mm/dd/yyyy format")
    while (validDate == False):
        date = input()
        try:
            realDate = time.strptime(date, "%m/%d/%Y")  #convert user input to time for later comparison
            validDate = True
        except:
            print("\nThe date you entered is invalid, please try again...\n")

    task.dueDate = str(realDate)

#----------------------------------------------------------------------#
    

#----------------------------Save-Funcs--------------------------------#
        
def savedTasksInit():
    try:
        with open("tasks.csv") as taskFile: #open save file to reinitialize each task at startup
            for line in taskFile:
                name = ""
                description = ""
                date = ""
                status = ""
                i = 0
                commacount = 0
                parenOpen = False
                if (line[i] != "\n"):
                    while (i < len(line)):
                        if (line[i] == '('):
                            parenOpen = True
                        elif (line[i] == ')'):
                            parenOpen = False
                        if (line[i] == ',' and parenOpen == False): #increment the current position being read
                            commacount += 1
                        elif (commacount == 0): # get task name from file
                            name += line[i]
                        elif (commacount == 1): # get description from file
                            description += line[i]
                        elif (commacount == 2): # get status from file
                            status += line[i]
                        elif (commacount == 3): #get due date from file
                            date += line[i]
                        i += 1
                    initTask(date,name,status,description) #pass read data from file to init function
            lines = taskFile.readlines()
            last = lines[-1]
            if(last != ""):
                f = open("tasks.csv", "a")
                f.write("\n")
                f.close()
        taskFile.close()
            
    except:
        print("Error opening save file (code:1)\n")



def initTask(date,name,status,description):
    
    curTask = Task()                                #create new task and add to list of tasks
    curTask.name = name                             #Set task values based on file data
    curTask.description = description
    curTask.dueDate = date
    curTask.status = status
    tasks.append(curTask)
    
    return

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

def saveTaskPos(task,pos):
    tasksOverwrite = ""
    with open("tasks.csv") as taskFile:
        i = 0
        for line in taskFile:
            if(i != pos): #rewrite all lines except the position specified
                tasksOverwrite += line
            else:
                tasksOverwrite += task.name + "," + task.description + "," + task.status + "," + str(task.dueDate)
            i += 1
    taskFile.close()
    f = open("tasks.csv", "w") #write over save file with new data
    f.write(tasksOverwrite)
    f.close()
    return

def saveTask(task): #override function for saving newly added tasks
    f = open("tasks.csv", "a") #append new task to end of file
    f.write(task.name + "," + task.description + "," + task.status + "," + str(task.dueDate) + "\n")
    f.close()
    return


#----------------------------------------------------------------------#

                
#----------------------------Search-Funcs------------------------------#

def search():
    returnToMenu = False
    while (returnToMenu == False):
        print("\nWhat would you like to search for?(\"/q to return\")\n")
        query = input()
        if(query == "/q"):
            returnToMenu = True
        exactSearch(query)
            
    return
    

def exactSearch(query):
    query = query.lower()
    index = 0
    for item in tasks:
        found = False
        i = 0
        try:
            while (i < len(item.name)): #if name contains search query display it
                if(item.name[i:i+len(query)].lower() == query):
                    found = True
                i += 1
            i = 0
            while (i < len(item.description)): #if description contains search query display it
                if(item.description[i:i+len(query)].lower() == query):
                    found = True
                i += 1
            if(found):
                displayTask(item, index)
        except:
            i = i
        index += 1
    return

#----------------------------------------------------------------------#

#----------------------------Menu-Funcs--------------------------------#

def mainMenu():
    programExit = False
    
    while(programExit == False):
        print("          Menu          \n------------------------\n1)    Today at a glance\n2)    Week at a glance\n3)    New task\n4)    Search tasks\n5)    Update task\n6)    View tasks\n7)    Last 10 Accomplishments\n8)    Quit\n-----------------------\n\nPlease select the desired action:")
        selected = input()
        if(selected == "1"):
            todayAtGlance()
        elif(selected == "3"):                        #if menu option 3 is chosen run the create task function
            createTask()
        elif(selected == "4"):
            search()
        elif(selected == "5"):
            updateTask()
        elif(selected == "8"):
            print("See you again soon!")
            programExit = True

def createTask():
    
    curTask = Task()                                #create new task and add to list of tasks
    tasks.append(curTask)

    setName(curTask)
    setDescription(curTask)
    setDate(curTask)
    saveTask(curTask)


    print("\nTask created successfully!\n")
    return

def displayTask(item,index):
    print("\n------------" + str(index) + "------------\n" + item.name + "\nDue on: " +  str(item.dueDate) + "\nStatus: " + item.status + "\n\n" + item.description + "\n-------------------------\n")
    return

def updateTask():
    
    exitFunc = False
    while(exitFunc == False): #until the user decides to leave continue
        
        validInput = False
        while(validInput == False): #determine if the user needs to search for the task to find its index
            print("\nDo you need to search for the task's index? (y/n)\n")
            userIn = input()
            if(userIn.lower() == "y"):
                search() #if indicated initiate search function
                validInput = True
            elif(userIn.lower() != "n"):
                print("Invalid entry, please try again.")
            else:
                validInput = True
                
        validInput = False
        while(validInput == False): #confirm the user inputed a valid integer to update
            print("\nPlease enter the index of the task you would like to update.\n")
            userIn = input()
            try:
                index = int(userIn)
                validInput = True
            except:
                print("Invalid entry, please try again.")

        validInput = False
        while(validInput == False): #determine what the user would like to update
            print("\nWhat would you like to update?\n1)   Name\n2)   Description\n3)   Status\n4)   Due Date\n5)   exit to menu\n")
            select = input()
            if(select == '1'):
                setName(tasks[index])
                saveTaskPos(tasks[index],int(index))
            elif(select == '2'):
                setDescription(tasks[index])
                saveTaskPos(tasks[index],int(index))
            elif(select == '3'):
                setStatus(tasks[index])
                saveTaskPos(tasks[index],int(index))
            elif(select == '4'):
                setDate(tasks[index])
                saveTaskPos(tasks[index],int(index))
            elif(select == '5'):
                validInput = True
            else:
                print("Invalid entry, please try again.")
        return

def todayAtGlance(): #display all tasks due today
    structTime = str(time.localtime())
    i = 17 #offset to speed up checks
    commaCount = 0
    today = ""
    while (i < len(structTime)):
        if (commaCount == 0 and structTime[i:i+7] == "tm_year"):
            i += 8
            while (structTime[i] != ","): #when in region for year note value for later comparison
                today += structTime[i]
                i += 1
            today += "/"
            commaCount += 1
        elif (commaCount == 1 and structTime[i:i+6] == "tm_mon"):
            i += 7
            while (structTime[i] != ","): #when in region for year note value for later comparison
                today += structTime[i]
                i += 1
            today += "/"
            commaCount += 1
        elif (commaCount == 2 and structTime[i:i+7] == "tm_mday"):
            i += 8
            while (structTime[i] != ","): #when in region for year note value for later comparison
                today += structTime[i]
                i += 1
            commaCount += 1
        elif (commaCount == 3):
            i = len(structTime)
        i += 1

    index = 0
    for task in tasks:
        taskDay = ""
        commaCount = 0
        structTime = str(task.dueDate)
        i = 17
        while (i < len(structTime)):
            if (commaCount == 0 and structTime[i:i+7] == "tm_year"):
                i += 8
                while (structTime[i] != ","): #when in region for year note value for later comparison
                    taskDay += structTime[i]
                    i += 1
                taskDay += "/"
                commaCount += 1
            elif (commaCount == 1 and structTime[i:i+6] == "tm_mon"):
                i += 7
                while (structTime[i] != ","): #when in region for year note value for later comparison
                    taskDay += structTime[i]
                    i += 1
                taskDay += "/"
                commaCount += 1
            elif (commaCount == 2 and structTime[i:i+7] == "tm_mday"):
                i += 8
                while (structTime[i] != ","): #when in region for year note value for later comparison
                    taskDay += structTime[i]
                    i += 1
                commaCount += 1
            elif (commaCount == 3):
                i = len(structTime)
            i += 1
        if(taskDay == today):
            displayTask(task,index)
        index += 1
        

#----------------------------------------------------------------------#


def main():

    savedTasksInit() #initialize array of tasks from save file
    mainMenu() #initialize main menu

    return 0

main()
