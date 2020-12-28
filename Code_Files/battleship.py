'''
There is a 4*4 board.
And the ship is randomly set on the board.
The player has 8 chances in total to guess the coordinate of the ship.
'''

from random import randint
def battleship(explorer):

    #set the board

    board = []

    for x in range(4):
        board.append(["O"] * 4)

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print("You have six chances\n\nBOARD")
    print_board(board)



    # randomly set the coordinate of ship

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print(ship_row)
    print(ship_col)



    # guess and show the result
    for Turn in range(8):
        print("Turn: " + str(Turn+1))
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            print("pass'code'")
            break
        else:
            if (guess_row < 0 or guess_row > 3) or (guess_col < 0 or guess_col > 3):
                print("That's not even a coordinate in the board")
            elif(board[guess_row][guess_col] == "X"):
                print("You already made that guess before")
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)
            if Turn==7:
                print("Game Over") #game over
