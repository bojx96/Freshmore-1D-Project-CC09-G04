import time
def prologue(name):
    with open("Prologue.txt", "r") as Prologue: #->If they allow text file, allow this, this is for line by line pop out
        prologuelines = Prologue.readlines()
        for line in prologuelines:
            print(line .format(name))
            time.sleep(0.5)

