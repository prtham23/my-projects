board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def display_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

def play_game():
    display_board()
    while True:
        handle_turn("X")
        display_board()
        if check_for_winner("X"):
            print("X wins!")
            break
        elif check_for_tie():
            print("Tie!")
            break
        handle_turn("O")
        display_board()
        if check_for_winner("O"):
            print("O wins!")
            break
        elif check_for_tie():
            print("Tie!")
            break

def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == " ":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player

def check_for_winner(player):
    for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_for_tie():
    if " " not in board:
        return True
    return False

play_game()
