
import random
the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print(u'\u2500' * 6)
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(u'\u2500' * 6)
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    player = 'X'
    count = 0

    print("The places in the board are numbered accordingly to numeric keypad so its look like:\n"
          " 7 | 8 | 9 \n 4 | 5 | 6 \n 1 | 2 | 3 ")
    for i in range(100):
        print_board(the_board)
        print("It's your turn " + player + ". To which place would you like to move? Please use only numbers 1-9 ")
        print()
        move = str(input())

        if the_board[move] == " ":
            the_board[move] = player
            count += 1

        else:
            print("That place is already filled.\n Choose a different place")
            if count == 9:
                print("\nGame Over.\n")
                print("It's a Tie!!")
                break
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':  # across the top
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':  # across the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':  # across the bottom
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':  # down the left side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':  # down the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':  # down the right side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + player + " won. ****")
                break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'
# restart = input("Do want to play Again?(y/n)")
# if restart == "y" or restart == "Y":

#
#     game()


#game()
