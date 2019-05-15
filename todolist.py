import json
import os

os.system("clear")
print("-------------------------------Todo-list CLI application-------------------------------")
def space():
    print(" ")
    print(" ")
    print(" ")
    print(" ")

def line_space():
    print("----")
space()
userlist = []

def maininput():
    while True:
        #Selecting if user wants to read or write the list, and or exit
        init_conf = input("Would you like to read or write your list? (read | write | exit)")
        #Customizing the list
        if init_conf == "write":
            uinput = input("What would you like to add to your list?")
            userlist.append(uinput)
            with open("userdata.json", "w") as write_file:
                json.dump(userlist, write_file)

         #Printing the list
        elif init_conf == "read":
            with open("userdata.json", "r") as read_file:
                data = json.load(read_file)
            for todo in data:
                line_space()
                print(todo)
                line_space()
                
        elif init_conf == "exit":
            break

maininput()
