import math

# Initialize the board and winning combinations
b = [" "] * 9
w = [
    [0, 1, 2],[3, 4, 5],[6, 7, 8],
    [0, 3, 6],[1, 4, 7],[2, 5, 8],
    [0, 4, 8],[2, 4, 6]
]

# Display the board
def show():
    print("\n".join(["|".join(b[i:i+3]) for i in range(0, 9, 3)]))

# Check if a player has won
def win(p):
    return any(all(b[i] == p for i in c) for c in w)

# Check if the board is full (draw)
def full():
    return " " not in b

# Minimax algorithm for AI decision making
def minimax(p):
    if win("O"): 
        return 1
    if win("X"): 
        return -1
    if full(): 
        return 0

    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = p
            scores.append(minimax("X" if p == "O" else "O"))
            b[i] = " "
    return max(scores) if p == "O" else min(scores)

# Find the best move for the computer (O)
def best():
    m, s = -1, -math.inf
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            sc = minimax("X")
            b[i] = " "
            if sc > s:
                s, m = sc, i
    return m

# Main game loop
def play():
    print("You: X, Computer: O")
    show()
    while True:
        h = int(input("Move (1-9): ")) - 1
        if b[h] != " ":
            print("Invalid move! Try again.")
            continue

        b[h] = "X"
        if win("X"):
            show()
            print("🎉 You win!")
            break
        if full():
            show()
            print("🤝 It's a draw!")
            break

        c = best()
        b[c] = "O"
        print(f"\nComputer moves at position {c + 1}")
        show()

        if win("O"):
            print("💻 Computer wins!")
            break
        if full():
            print("🤝 It's a draw!")
            break


# Start the game
play()      