from character_create import character_profile
import random
import time
from computer_access import check_userid
from prologue_readtext import prologue
from enter_room import enter_room

def prologue_start():
    name = input("Please input your name: ")
    sex_num = input("Sex?:\n1)Male\n2)Female\n3)Binary\n4)Yes please\n")
    character_profile(name,sex_num)
    time.sleep(1)

    prologue(name)
    enter_room(name)
    print("\n")

    # Prologue(name) #This is the python function in replacement of txt file, This is for instant pop out
    # Prologue2(name) #This is the python function in replacement of txt file, this is for line by line pop out
    # print(Prologue.read().format(name)) #->If they allow text file, allow this, this is for instant pop out

    # print("{} enters Dr.Jerry's Lab. It was oddly clean, although with a slight stench".format(name) )
    # print("{}: I guess he love his bananas, the bins are filled with those.".format(name) )
    # print("On the corner of the Lab, the still flickering screen left by Dr.Jerry caught your eye.")
    # print("{}: Looks like I will have to check his PC.. Hope its easy to get in.".format(name) )
    # print("\n")

    user_id = input("Enter username: ") #By Georgia, edited by Brandon
    check_userid(user_id)
