import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for winner
def winner(b, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8], # rows
        [0,3,6],[1,4,7],[2,5,8], # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_states)

# Check if board full
def full_board(b):
    return ' ' not in b

# Minimax Algorithm
def minimax(b, depth, is_maximizing):
    if winner(b, 'O'):  # AI win
        return 1
    elif winner(b, 'X'):  # Human win
        return -1
    elif full_board(b):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth+1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth+1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI Move
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Main Game Loop
def play():
    print("Tic Tac Toe! You are X, AI is O.")
    print_board()

    while True:
        # Human turn
        move = int(input("Enter your move (0-8): "))
        if board[move] == ' ':
            board[move] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        print_board()
        if winner(board, 'X'):
            print("You win!")
            break
        if full_board(board):
            print("It's a draw!")
            break

        # AI turn
        best_move()
        print("AI Move:")
        print_board()
        if winner(board, 'O'):
            print("AI wins!")
            break
        if full_board(board):
            print("It's a draw!")
            break

play()
