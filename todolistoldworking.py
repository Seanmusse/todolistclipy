import pickle
import os

os.system("clear")
print("-------------------------------Todo-list CLI application-------------------------------")
def space():
    print(" ")
    print(" ")
    print(" ")
    print(" ")

space()
userlist = []
filename = "userdata.p"

def maininput():
    loaded_uinput = []
    while True:
        #Selecting if user wants to read or write the list, and or exit
        init_conf = input("Would you like to read or write your list? (read | write | exit)")
        #Printing the list
        if init_conf == "read":
            pickle_in = open(filename, "rb")
            loaded_uinput = pickle.load(pickle_in, encoding='bytes')
            pickle_in.close()
            print(*loaded_uinput, sep="\n")
        #Customizing the list
        elif init_conf == "write":
            uinput = input("What would you like to add to your list?")
            userlist.append("-" + uinput)
            pickle_out = open(filename, "ab")
            pickle.dump(userlist, pickle_out)
            pickle_out.close()
            print(*loaded_uinput, sep="\n")
        elif init_conf == "exit":
            break

maininput()
