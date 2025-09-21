import random, time

N = 5
grid = [['-' for _ in range(N)] for _ in range(N)]

# Place obstacles
for _ in range(5):
    r,c = random.randint(0,N-1), random.randint(0,N-1)
    grid[r][c] = '#'

# Place tasks
for _ in range(3):
    r,c = random.randint(0,N-1), random.randint(0,N-1)
    if grid[r][c] == '-': grid[r][c] = 'T'

# Place agent
agent = (0,0)
collected = 0

def show():
    for row in grid: print(' '.join(row))
    print()

for step in range(10):
    r,c = agent
    # Collect task if present
    if grid[r][c] == 'T':
        collected += 1
        print("Task collected! Total =", collected)
    grid[r][c] = 'A'
    show()

    # Reflex move
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    random.shuffle(moves)
    for dr,dc in moves:
        nr,nc=r+dr,c+dc
        if 0<=nr<N and 0<=nc<N and grid[nr][nc]!='#':
            grid[r][c]='-'
            agent=(nr,nc)
            break
    time.sleep(0.9)

print("Final Collected Tasks:", collected)
