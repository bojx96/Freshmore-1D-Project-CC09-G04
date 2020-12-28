import time
def enter_room(name):

    text = "\n\n{} enters Dr.Jerry's Lab. It was oddly clean, although with a slight stench\n\
{}: I guess he love his bananas, the bins are filled with those.\n\
On the corner of the Lab, the still flickering screen left by Dr.Jerry caught your eye.\n\
{}: Looks like I will have to check his PC.. I hope its easy to get in.".format(name,name,name)


    a = text.split("\n")
    for i in a:
        print(str(i))
        time.sleep(0.5)
    return