import os
import time
import random


game_board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def display_board():
    print("   |   |   ")
    print(f" {game_board[1]} | {game_board[2]} | {game_board[3]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {game_board[4]} | {game_board[5]} | {game_board[6]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {game_board[7]} | {game_board[8]} | {game_board[9]} ")
    print("   |   |   ")


def check_winner(board, mark):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  
        (1, 5, 9), (3, 5, 7)             
    ]
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_conditions)


def board_is_full(board):
    return " " not in board[1:]


def get_computer_move(board):
    if board[5] == " ":
        return 5

    empty_spaces = [i for i, spot in enumerate(board) if spot == " " and i != 0]
    return random.choice(empty_spaces) if empty_spaces else 5


while True:
    os.system("cls" if os.name == "nt" else "clear")
    display_board()

    
    try:
        player_move = int(input("Player X, choose an empty space (1-9): "))
        if 1 <= player_move <= 9 and game_board[player_move] == " ":
            game_board[player_move] = "X"
        else:
            print("Sorry, that space is not empty!")
            time.sleep(1)
            continue
    except ValueError:
        print("Please enter a number between 1 and 9.")
        time.sleep(1)
        continue

    if check_winner(game_board, "X"):
        os.system("cls" if os.name == "nt" else "clear")
        display_board()
        print("Player X wins! Congratulations!")
        break

    if board_is_full(game_board):
        print("TIE!")
        break

    
    print("Opponent is making a move...")
    time.sleep(1)
    computer_move = get_computer_move(game_board)
    game_board[computer_move] = "O"

    if check_winner(game_board, "O"):
        os.system("cls" if os.name == "nt" else "clear")
        display_board()
        print("Player O wins! UH OH. TRY AGAIN")
        break

    if board_is_full(game_board):
        print("TIE!")
        break
