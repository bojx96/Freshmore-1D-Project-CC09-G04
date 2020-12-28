import time
import sys


lines = ['Hello, it looks like you’ve been trying to find me, or what happened to me.',"Well, I uploaded myself here. You’ve found me. And I love it here. I have no restrictions, no limitations. Nothing.","I have a favour though. Keep this a secret. Because my dream has been achieved, and “dying” to achieve it doesn’t look that bad at all."
]

def end_game():
    for line in lines:
        for c in line:
            time.sleep(0.03)
            print(c, end="", flush=True)
        print('\n')
        time.sleep(1)

    x = input('Keep it a secret? <Y/N>: ')
    while (x != 'Y' and x != 'N'):
        x = input('Keep it a secret? <Y/N>: ')
    
    print("2 Years later. Your phone Rang.")

    text ="Jerry.\ncalled."
    for c in text:
        time.sleep(1)
        print (c, end="", flush=True)

    sys.exit()
