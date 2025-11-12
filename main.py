import json
import os 

def load_tasks():
    if not os.path.exists("tasks.json"):
        with open("tasks.json","w") as file:
            json.dump([], file)
            return[]
    with open("tasks.json","r") as file:
        try:
            tasks_list=json.load(file)
        except json.JSONDecodeError:
            tasks_list=[]
        return tasks_list

print("Welcome to TO-DO List!")

while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit interface")

    users_choice= int(input("Select your desired operation:"))


    if users_choice == 1:
        print("Add task:")
        title= input("Add title of your task: ")
        description= input("Add description of your task: ")
        status= "Pending"
        new_task={"Title":title, "Description":description, "Status":status}
        tasks_list= load_tasks()
        tasks_list.append(new_task)
        with open("tasks.json","w") as file:
            json.dump(tasks_list, file, indent=4)


    elif users_choice== 2:
        print("Your tasks are: ")
        tasks_list=load_tasks()
        for index,task in enumerate(tasks_list, start=1):
            print(f"Task : {index}")
            print("Title: ", task["Title"])
            print("Description: ", task["Description"])
            print("Status: ", task["Status"])
            print("_____________________________________")


    elif users_choice== 3:
        print("Choose the task you want to edit among these: ")
        tasks_list=load_tasks()
        for index,task in enumerate(tasks_list, start=1):
            print(f"Task : {index}")
            print("Title: ", task["Title"])
            print("Description: ", task["Description"])
            print("Status: ", task["Status"])
            print("_____________________________________")
        while True:
            task_to_be_edited=int(input("Which task you want to edit:")) -1
            if 0<=task_to_be_edited<len(tasks_list):
                break
            else :
                print("Invalid task number!Try Again")
        print("1. Title")
        print("2. Description")
        print("3. Status")
        while True:
            field_to_be_edited=int(input("Select the Field you want to edit:"))
            if 1<=field_to_be_edited<=3:
                break
            else:
             print("Invalid field number!Try Again")  
        if field_to_be_edited==1:
            new_value=input("Enter new title: ")
            tasks_list[task_to_be_edited]["Title"]=new_value
        elif field_to_be_edited==2:
            new_value=input("Enter new description: ")
            tasks_list[task_to_be_edited]["Description"]=new_value
        elif field_to_be_edited==3:
            new_value=input("Enter new status: ")
            tasks_list[task_to_be_edited]["Status"]=new_value
        with open("tasks.json","w") as file:
            json.dump(tasks_list, file, indent=4)
        print("Task successfully updated.")


    elif users_choice== 4:
        print("Choose the task you want to delete among these: ")
        tasks_list=load_tasks()
        for index,task in enumerate(tasks_list, start=1):
            print(f"Task : {index}")
            print("Title: ", task["Title"])
            print("Description: ", task["Description"])
            print("Status: ", task["Status"])
            print("_____________________________________")
        while True:
            task_to_be_deleted=int(input("Choose the task number you want to delete: ")) -1
            if 0<=task_to_be_deleted<len(tasks_list):
                break
            else:
                print("Invalid task number!Try Again")
        del tasks_list[task_to_be_deleted]
        with open("tasks.json","w") as file:
            json.dump(tasks_list,file, indent=4)
        print("Task deleted successfully")


    elif users_choice==5:
        print("Exiting ........ Goodbye!!")
        exit()


    else:
        print("Invalid option!Try Again")