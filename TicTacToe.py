from os import system
from random import randint


def clear_output():
    return system('cls')


def display_board(board):
    # clears command console
    clear_output()
    # Initialise 3x3 board
    print(board[7] + " # " + board[8] + " # " + board[9])
    print("#" * 9)
    print(board[4] + " # " + board[5] + " # " + board[6])
    print("#" * 9)
    print(board[1] + " # " + board[2] + " # " + board[3])


def player_input():
    # This function asks player 1 to  choose 'X' or 'O'
    char = ''

    while char != ("X" or "O"):
        char = input("Player 1 please choose X or O ").upper()
        player1 = char

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return player1, player2


def place_marker(board, marker, pos):
    board[pos] = marker


def win_check(board, mark):
    # this function checks if player has won
    return (
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark)
    )


def choose_first():
    # Import random.int to randomly choose player 1 or 2
    if randint(1, 2) == 1:
        return "player 1"
    else:
        return "player 2"


def space_check(board, pos):
    # checks for  blank spaces on the board for any position called
    return board[pos] == " "


def full_board_check(board):
    # Checks if the board is completely filled up
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    # Ask the player for the next position on the board
    # If the position is already filled, ask the player again for another position
    pos = 0
    while pos not in range(1, 10) or not space_check(board, pos):
        pos = int(input("Please key in a position value (0-9) "))

    return pos


def replay():
    # Ask Players if they would like to play again
    answer = input("Would you like to play again? Key Y for Yes or N for No ").upper()
    if answer == "Y":
        return True
    else:
        return False


def main():
    # Runs als the functions for the program
    print('Welcome to Tic Tac Toe!')

    while True:
        # Ask the players if they are ready to start the game
        start = input("Are you ready to play the game? Key Y to start N to exit ").upper()
        if start == "Y":
            game = True
        else:
            break

        # Generates variables for the game
        play_field = [" "] * 10
        player1_char, player2_char = player_input()
        player_turn = choose_first()

        while game:
            # Shows the playing field
            display_board(play_field)

            if player_turn == "player 1":
                # Player 1 turn
                print("Player 1")
                pos = player_choice(play_field)
                place_marker(play_field, player1_char, pos)

                if win_check(play_field, player1_char):
                    display_board(play_field)
                    print("Player 1 won!")
                    game = False

                else:
                    if full_board_check(play_field):
                        display_board(play_field)
                        print("Its a Tie!")
                        break
                    else:
                        player_turn = "player 2"

            else:
                # Player 2 turn
                print("Player 2")
                pos = player_choice(play_field)
                place_marker(play_field, player2_char, pos)

                if win_check(play_field, player2_char):
                    display_board(play_field)
                    print("Player 2 won!")
                    game = False

                else:
                    if full_board_check(play_field):
                        display_board(play_field)
                        print("Its a Tie!")
                        break
                    else:
                        player_turn = "player 1"

        if not replay():
            break


if __name__ == "__main__":
    main()
