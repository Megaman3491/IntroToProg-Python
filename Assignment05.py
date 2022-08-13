'''
******************************************************
Tittle    : Saving Multiple Data To txt

Dev       : Fanuel

Date      : August 10, 2022

ChangeLog : Fanuel, 8/10/2022, Created File
******************************************************
'''
StrTask     = None
StrPriority = None
ObjFile     = None
ListFile    = []

while(True):
    print   ("What would you like to do?")
    Choice = input("Write data (w) Read data (r) and (exit) to Exit: ")
    Choice.lower()

    if Choice == "w":
        StrTask     = input("What Is your task    : ")
        StrPriority = input("What is your priority: ")
        Data        = { "Task" : StrTask , "Priority" : StrPriority}
        ListFile.append(ObjFile)
        ObjFile = open("ToDoList.txt", "a")
        ObjFile.write(Data["Task"] + "," + Data["Priority"] + "\n")
        ObjFile.close()

    elif Choice == "r":
        ObjFile = open("ToDoList.txt", "r")
        for row in ObjFile:
            Listrow = row.split(",")
            Dicrow  = {"Task" : Listrow[0], "Priority" : Listrow[1].strip()}
            print (Dicrow)

    elif Choice == "exit":
        break


    else:
        print("Please chose the told options!")

















