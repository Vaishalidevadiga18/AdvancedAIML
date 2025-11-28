# minimax
import math

# Define players
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Initialize board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Display the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if there are moves left
def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

# Evaluate board state
def evaluate(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != EMPTY:
            return 10 if row[0] == AI else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return 10 if board[0][col] == AI else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == AI else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == AI else -10

    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Terminal states
    if score == 10: return score - depth   # Prefer faster wins
    if score == -10: return score + depth  # Prefer slower losses
    if not is_moves_left(board): return 0  # Draw

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

# Find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Example play (AI vs Human input)
if __name__ == "__main__":
    board = create_board()
    print("Tic Tac Toe: You are O, AI is X")
    print_board(board)

    while True:
        # Human move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != EMPTY:
            print("Invalid move, try again.")
            continue
        board[row][col] = HUMAN
        print_board(board)

        if evaluate(board) == -10:
            print("You win!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI move
        move = find_best_move(board)
        board[move[0]][move[1]] = AI
        print("AI plays:")
        print_board(board)

        if evaluate(board) == 10:
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break