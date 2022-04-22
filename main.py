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
    turn = 'X'
    count = 0

    print("The places in the board are numbered accordingly to numeric keypad. so its look like:\n"
          " 7 | 8 | 9 \n 4 | 5 | 6 \n 1 | 2 | 3 ")

    for i in range(10):
        print_board(the_board)
        print("It's your turn," + turn + ". Move to which place?")
        print()
        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\n Choose a different place")
            continue

        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':  # across the top
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':  # across the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':  # across the bottom
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':  # down the left side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':  # down the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':  # down the right side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in the_board:
            the_board[key] = " "

        game()


game()
