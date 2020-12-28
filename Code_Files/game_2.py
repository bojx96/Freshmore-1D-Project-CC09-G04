#!/usr/bin/env python
# coding: utf-8

# In[10]:


from random import seed
from random import choice

def game_2(explorer):

    print('''Good Job getting through that first puzzle there. Now's time for the second puzzle!
    I hope you like math because this next one requires you to work out some equations.\n''')

    print("I would recommend that you prepare a pen and paper for this problem as it might be hard to solely rely on mental sums hehe\n")


    user_input = input("Are you ready? Type in Yes or No: ")

    while user_input != "Yes" and user_input != "yes":
        x1 = "Don't be worried! I'll be nice! Maybe... hehe"
        x2 = "Come onnnnnn I know you're smart enough to handle it!"
        x3 = "Are you not at least curious as to what happened to me?\nChoose something else!\n"
        responses = [x1,x2,x3]
        selection = choice(responses)
        print(selection)
        user_input = input("Are you ready to begin? Key in Yes or No: ")

    if user_input == "Yes" or user_input == "yes":
        print("That's great! Now, onto the next section!\n")

    print("Here's the riddle:\n")

    print('''A small number of cards has been lost from a complete pack.
    If I deal among four people, three cards remain.
    If I deal among three people, two remain and if I deal among five people, two cards remain.
    How many cards are there? (A pack of cards contain 52 cards)''')

    user_input1 = input("Answer: ")
    user_response1 = user_input1
    a1 = "Incorrect Answer! Try Again!"
    a2 = "Not quite there yet! Try again!"
    a3 = "Not there yet! Here's a quick hint: You might want to consider the different cases!"
    fixed_answers = [a1,a2]
    hinted_answer = a3

    seed(1)
    count = 0
    while count < 2:
        if user_response1 != '47':
            final_response = choice(fixed_answers)
            print(final_response)
            count += 1
            user_input1 = input("Answer: ")
            user_response1 = user_input1

        else:
            print("That's Correct! Tip: You may wish to take down this answer. It might come in handy later on!")
            break

    while count >= 2:
        if user_response1 != '47':
            final_response1 = hinted_answer
            print(final_response1)
            count += 1
            user_input1 = input("Answer: ")
            user_response1 = user_input1
        else:
            print("That's Correct! Tip: You may wish to take down this answer. It might come in handy later on!")
            break












# In[ ]:
