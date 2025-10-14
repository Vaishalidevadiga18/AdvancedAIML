import math

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

# Check if a player has won
def winner(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for state in win_states:
        if all(board[i] == player for i in state):
            return True
    return False

# Check if board is full
def is_full(board):
    return all(s != " " for s in board)

# Evaluate the board
def evaluate(board):
    if winner(board, "O"):  # AI is "O"
        return 1
    elif winner(board, "X"):  # Human is "X"
        return -1
    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Terminal states
    if score == 1:
        return score
    if score == -1:
        return score
    if is_full(board):
        return 0

    if is_maximizing:  # AI turn (O)
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best_score = max(best_score, minimax(board, depth+1, False))
                board[i] = " "
        return best_score
    else:  # Human turn (X)
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best_score = min(best_score, minimax(board, depth+1, True))
                board[i] = " "
        return best_score

# Find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    board = [" "] * 9
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move, try again.")
            continue
        board[move] = "X"
        print_board(board)

        if winner(board, "X"):
            print("You win! 🎉")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "O"
        print("AI plays at:", ai_move)
        print_board(board)

        if winner(board, "O"):
            print("AI wins! 🤖")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
