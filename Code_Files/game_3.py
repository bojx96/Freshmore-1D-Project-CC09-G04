#!/usr/bin/env python
# coding: utf-8

# In[26]:


from random import seed
from random import choice
def game_3(explorer):
    print("Hey! You've made it this far into the story, congrats! You're doing fineeeeeeee. Are you ready for the next challenge?\nHint: You might want to grab a pen and paper for this ;)\n")

    print("Here are some questions for you! I hope you're good at Riddles haha! Are you ready to begin?")

    option = input("Are you ready to begin? Key in Yes or No: ")
    answer = option

    seed(1)
    while option != "Yes" and option != "yes":
        x1 = "Come on, you made it this far already, give it a try!\nLet me ask you again\n"
        x2 = "Pleaseeeee... Don't be such a killjoy!\n"
        x3 = "Don't you wanna find out what happened to me?\nChoose something else!\n"
        responses = [x1,x2,x3]
        selection = choice(responses)
        print(selection)
        option = input("Are you ready to begin? Key in Yes or No: ")

    if option == "Yes" or option == "yes":
        print("Yes! That's the spirit! Now, let us begin!\n")

    response1 = input("A. Okay! B. I guess I'll try... C. Please give me something easy!! ")
    responseback1 = response1

    if responseback1 == "A" :
        print("I like your enthusiasm there! Let's proceed!")
    elif responseback1 == "B" or "C":
        print("I'm sure you'll be fine! Let's proceed!")

    print("Here's the first riddle!\n")

    print('''This thing all things devours;
    Birds, beasts, trees, flowers;
    Gnaws iron, bites steel;
    Grinds hard stones to meal;
    Slays king, ruins town,
    and beats mountains down.''')

    response2 = input("Answer: ")
    responseback2 = response2

    a1 = "Nice Try! But the answer's wrong sadly... How bout you give it another go?"
    a2 = "Oof. Not quite there yet!. Try again!"
    a3 = "Not there yet! Here's a quick hint: This riddle is from a very famous movie!"
    a4 = "Almost there! Here's another hint: The answer can be derived from looking at a watch or a clock."
    a5 = "Nope! Here's another hint: You encounter it daily."
    fixed_answers = [a1,a2]
    variable_answers = [a3,a4,a5]

    seed(1)
    count = 0
    while count < 2:
        if responseback2 != "Time" and responseback2 != "time":
            final_response = choice(fixed_answers)
            print(final_response)
            count += 1
            responseback2 = input("Answer: ")
        else:
            print("That's Correct! Tip: You may wish to take down this answer. It might come in handy later on!")
            break

    while count >= 2:
        if responseback2 != "Time" and responseback2 != "time":
            final_response1 = choice(variable_answers)
            print(final_response1)
            responseback2 = input("Answer")
        else:
            print("That's Correct! Tip: You may wish to take down this answer. It might come in handy later on!")
            break












# In[ ]:
