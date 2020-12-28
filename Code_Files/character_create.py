#Done by Brandon

import time

def character_profile(name,sex_num):
    counter = 0
    sex = ''
    # name = input("Please input your name: \n")
    # print("Your name is {}".format(name))
    # sex_num = input("Sex?:\n1)Male\n2)Female\n3)Binary\n4)Yes please\n")

    while (sex_num not in ['1','2','3','4']):
                bool1 = True
                while(bool1):
                    sex_num = input("Input is invalid, please input an integer\n")
                    if (sex_num == '1' or sex_num == '2' or sex_num == '3' or sex_num == '4'):
                        bool1 = False

    while (sex_num in ['1','2','3','4'] and sex == ''):
        if (sex_num == '1'):
            sex = 'Male'
        
        elif (sex_num == '2'):
            sex = 'Female'
            
        elif (sex_num == '3'):
            sex = '01101011 01110101 01100101 01101000'

        elif (sex_num == '4'):
            counter += 1

            if (counter < 3):
                print("Kinky, but lets get down to business here")

            elif (counter >= 3 and counter < 8):
                print("Quit screwing around this time alright?")
            
            elif (counter >= 8 and counter < 12):
                print("Seriously. STOP SCREWING AROUND!!!")
            
            elif (counter >= 12):
                print("Arg, FINEEEEEEE, 'YES PLEASEEEEEEEEE' IT IS! ")
                sex = 'Yes please'
                break
            sex_num = input("Sex?:\n1)Male\n2)Female\n3)Binary\n4)Yes please\n")
            if (sex_num not in ['1','2','3','4']):
                print("Nvm, I will pick it for you, your sex is a 'Burden'.")
                sex = 'Burden'

    print("Your name is: {}\nYour sex is: {}".format(name,sex))
    time.sleep(1)
    if (sex == 'Yes please'):
        text = "Actually only your name mattered. Wanted to get to know you more but.. arg.. 'YeS pLeAsE'..\n\n\n\n"
    elif (sex == 'Burden'):
        text = "Actually only your name mattered. But someone just couldn't read instructions carefully right?!\n\n\n\n"
    else:
        text = "Only your name was important actually. The latter was redundant. Just wanted to get to know you more. *winkwink*\n\n\n\n"

    for c in text:
        time.sleep(0.01)   
        print( c , end="", flush=True)

    return name,sex
