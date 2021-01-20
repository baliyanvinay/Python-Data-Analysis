# Scope of the project:
# 1: Print a board,
# 2: Take in Player Input,
# 3: Place their input on board,
# 4: Check if the game is won, tied, lost or ongoing
# 5: Repeat step 3 and 4 until the game is won or tied,
# 6:Ask if the players wants to play again.

# Print a board: Write a function that prints out a board. Setup you board as a list, each index 1-9 corresponds with a number
# on a number pad, so you get a 3 by 3 board representation.
from IPython.display import clear_output


def display_board(board):
    # range from 1 to 4 only so that it skips '#' and then prints first rows and so on
    for index in range(1, 4):
        print(str(board[index]) + '|' +
              str(board[index+3]) + '|' + str(board[index+6]))
# end of display_board function

# test_board=['#','X','O','X','O','X','O','X','O','X']
# hash is added to the list so that the index can start from 1


def player_selection():
    # accepting strings only within quotes
    player1 = input("Please pick a marker 'X' or 'O': ")
    print('You shall be Player 1')
    if player1 == 'X':
        player2 = 'O'
    else:
        player1, player2 = 'O', 'X'
    return player1, player2
# End of player_selection function


def player_input():
    pos = int(input('Please enter position between 1-9: '))
    if pos in range(1, 10):
        return pos
    else:
        print('Position out of range of board: Try again!')
        return player_input()  # recursion of function
# player_input() # to get input from user


def place_marker():
    step = 0  # for the steps both players can take during the game
    while step < 9:
        step += 1
        pos = player_input()
        if input_board[pos] != ' ':
            step -= 1
            print('Position already occupied')
            # to cover cases where a player can't update an already filled position
            continue
        else:
            if step % 2 != 0:
                input_board[pos] = p1
            else:
                input_board[pos] = p2
        # board is displayed as soon as we have values within while loop
        clear_output()
        display_board(input_board)
        if check_input_board(input_board) == True:
            print('You have won!')
            break
        else:
            pass
# end of place_marker function


def check_input_board(check_board):
    if ((check_board[1] == check_board[4] == check_board[7] and check_board[1] != ' ')
        or (check_board[1] == check_board[2] == check_board[3] and check_board[1] != ' ')
        or (check_board[3] == check_board[6] == check_board[9] and check_board[3] != ' ')
        or (check_board[7] == check_board[8] == check_board[9] and check_board[7] != ' ')
        or (check_board[2] == check_board[5] == check_board[8] and check_board[2] != ' ')
        or (check_board[1] == check_board[5] == check_board[9] and check_board[1] != ' ')
        or (check_board[3] == check_board[5] == check_board[7] and check_board[3] != ' ')
            or (check_board[4] == check_board[5] == check_board[6] and check_board[4] != ' ')):
        return True
    else:
        return False
# end of check_input_board function


# Final Flow of the program:: All other functions are being called here
input_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# empty list for the values of input board
display_board(input_board)
# board displayed just for the first time
p1, p2 = player_selection()  # will get which player is choosing what
choice = 'Y'
while choice == 'Y':
    place_marker()  # to fill out the values of input string
    choice = input('Do you want to play again? (Y/N) :')
# end of place_marker() function
# END OF PROJECT TIC TAC TOE :: 27-Apr-2020 to 28-Apr-2020
