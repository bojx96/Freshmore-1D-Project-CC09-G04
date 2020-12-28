#Done by Georgia
import time
# user_id = input("Enter username: ") #-> This is shifted into main_game
correct_id = "jerry"
correct_pwd = "14021951"

def check_userid(user_id):
    bool2 = True
    # if user_id != correct_id: -> Actually redundant
        # bool2 = True -> shift upwards

    if (user_id.lower().strip() == correct_id): # -> Added this for the else
        pass

    else: # -> This is such that if the user_id correct, it will just pass to guess password function, if wrong, the while loop triggers
        while bool2:
            for j in range (4):
                sikeu = ""
                if j == 1:
                    sikeu = ". Username is case sensitive."
                if j == 2:
                    sikeu = ". Try again! Hint: Read the prologue."
                if j == 3:
                    sikeu = ". Read the prologue THOROUGHLY!"

                print ("INCORRECT USERNAME" + sikeu)
                user_id = input("Re-enter username(case-sensitive): ")

                if user_id == correct_id:
                    bool2 = False
                    break

    pwd = input("Enter password: ")
    # correct_pwd = "jerryisthebest" ->Shift upwards

    def check_password(pwd):
        bool1 = True
        # if pwd != correct_pwd: -> Actually redundant
        #     bool1 = True -> Shifted upwards

        #if (pwd == correct_pwd):
            #print('password guessed')
            #return "Damn you got it" # -> This makes sure that it doesnt go into the while loop but end the function

        while bool1:
            i = 0
            sike = '.'

            if pwd == correct_pwd:

                bool1 = False
                print('Login details authenticated')
                time.sleep(0.8)
                print('Logging in', end="", flush=True)
                text = '.....'
                for c in text:
                    time.sleep(0.8)
                    print(c, end="", flush=True)
                print("\n")
                text = 'Successfully logged in'
                for c in text:
                    time.sleep(0.05)
                    print(c, end="", flush=True)
                print("\n")

                print("Welcome. Type help and press enter to view a list of commands.")
                sike = ""


            else:
                if i == 1:
                    sike = ". Try again!"
                if i == 2:
                    sike = ". There's a hint in the prologue!"
                if i == 3:
                    sike = ". The password has 8 characters."
                print ("INCORRECT PASSWORD" + sike)
                i += 1
                pwd = input("Re-enter password: ")







    check_password(pwd)
    return "Good Job"
# ID = check_userid(user_id)
# print (ID)
