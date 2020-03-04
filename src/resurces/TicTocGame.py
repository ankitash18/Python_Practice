# Milestone Project 1: Full Walk-through Code Solution
#print('\n'*100)


#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
#We need to print a board.
#Take in player input.
#Place their input on the board.
#Check if the game is won,tied, lost, or ongoing.
#Repeat c and d until the game has been won or tied.
#Ask if players want to play again.


def display_board(board):
    print('\n' * 100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

#test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
#display_board(test_board)


##**Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer


def player_input():
    marker =''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1.choose X or O:').upper()

    if marker =='X':
       return('X','O')
    else:
         return('O','X')


#player1_marker,player2_marker = player_input()


##Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.


def place_marker(board,marker,position):
    board[position] = marker

#place_marker(test_board,'$',8)

#display_board(test_board)

#Step 4: Write a function that takes in a board and checks to see if someone has won.

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle\n",
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle\n",
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side\n",
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal\n",
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal"


#display_board(test_board)
#print(win_check(test_board,'X'))

#Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.*


import random

def  choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


#Write a function that returns a boolean indicating whether a space on the board is freely available.


def space_check(board,position):
    return board[position] == ' '

#Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
     # board is full reur true
    return True

# Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.

def player_choice(board):
    position  = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not  space_check(board,position):
        position = int(input('choose a position:(1-9)'))

    return position


#Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**


def replay():

    choice = input('play again? Enter Yes or No')

    return choice == 'Yes'

#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

#while loop to keeo running the game

print('Wlcome to Tic Toc Toe')
while True:
    #play the game
    #set everything up(board,markers,who fisrt)

    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn +'Will go first')

    play_game = input('Ready to Play? y or n?')

    if play_game =='y':
        game_on = True
    else:
        game_on = False


    #game play
    while game_on:
         # show the broad
        if turn == 'Player 1':
            display_board(the_board)
            #choose a broad

            position =  player_choice(the_board)

         #chose a marker on position
            place_marker(the_board,player1_marker,position)

            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('the game is Tie')
                    game_on = False
                else:
                    turn = 'Player 2'

            #check if there is tie

            #no tie n no win ,ten next playe turn
        else:
            display_board(the_board)
            # choose a broad

            position = player_choice(the_board)

            # chose a marker on position
            place_marker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('the game is Tie')
                    game_on = False
                else:
                    turn = 'Player 1'

        if not replay():
            break



#break out of while loop on replay(



