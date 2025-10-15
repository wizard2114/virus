import math

board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|'.join(row))
        print("-" * 5)

# Function to check for a win
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move using Minimax algorithm
def ai_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'X'

# Function to play the game
def play_game():
    while True:
        print_board()
        if check_win(board, 'X'):
            print("X wins!")
            break
        elif check_win(board, 'O'):
            print("O wins!")
            break
        elif ' ' not in board:
            print("It's a tie!")
            break

        move = input("Enter your move (1-9): ")
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid move. Try again.")
            continue
        move = int(move) - 1
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'O'

        ai_move(board)

# Start the game
play_game()
