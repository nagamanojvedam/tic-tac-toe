position_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def check_winner(board=[], pattern=""):
    if board[0] + board[1] + board[2] == pattern:
        return True
    elif board[3] + board[4] + board[5] == pattern:
        return True

    elif board[6] + board[7] + board[8] == pattern:
        return True

    elif board[0] + board[3] + board[6] == pattern:
        return True

    elif board[1] + board[4] + board[7] == pattern:
        return True

    elif board[2] + board[5] + board[8] == pattern:
        return True

    elif board[0] + board[4] + board[8] == pattern:
        return True

    elif board[2] + board[4] + board[6] == pattern:
        return True
    else:
        pass


def display_board(board=[]):
    print()
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print()


def players_choice():
    player_choice = input("Do you want to start game? [Y/N] : ")

    if player_choice.lower() in ["y", "n"]:
        return player_choice
    else:
        print("Enter valid choice. [Y/N] : ")
        return players_choice()


def play_again():
    player_choice = input("Do you want to play again? [Y/N] : ")

    if player_choice.lower() == "y":
        return start_game()
    elif player_choice.lower() == "n":
        print("Thanks for playing.")
        exit()
    else:
        print("Enter valid selection.")
        return play_again()


def set_board():
    global game_board
    game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    global marked_positions
    marked_positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    global count
    count = 1


def verify_position(player):
    st = input(f"Enter {player} position : ")

    if st in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return int(st)
    else:
        print("Choice should be from 1 to 9...")
        return verify_position(player)


def take_position(player=""):
    position = verify_position(player)

    if 1 <= position <= 9:
        if marked_positions[position - 1] == " ":
            marked_positions[position - 1] = player
            global count
            count += 1
            game_board[position - 1] = player
        else:
            print("Position already taken.")
            take_position(player)
    else:
        print("Enter correct position.")
        take_position(player)


def start_game():
    print("Welcome to Tic-Tac-Toe")
    set_board()
    display_board(game_board)
    player_interest = players_choice()

    if player_interest.lower() == "n":
        print("Thanks for playing")
        exit()
    else:
        while True:
            if count <= 9:
                print()
                take_position("X")
                if check_winner(game_board, "XXX"):
                    print("X won the game")
                    display_board(game_board)
                    play_again()
                display_board(game_board)

                if count == 10:
                    continue

                take_position("O")
                if check_winner(game_board, "OOO"):
                    print("O won the game")
                    display_board(game_board)
                    play_again()
                display_board(game_board)
            else:
                print("Draw Game!")
                play_again()


if __name__ == "__main__":
    start_game()
