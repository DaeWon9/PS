import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def is_movable(row, col):
    return (0 <= row < n and 0 <= col < n)

def get_idx(row, col):
    return row * n + col

def solve(row, col):
    idx = get_idx(row, col)
    if (idx in memo):
        return memo[idx]
    
    memo[idx] = 1 
    for i in range(4):
        dr = row + direction_y[i]
        dc = col + direction_x[i]
        if (is_movable(dr, dc) and board[row][col] < board[dr][dc]):
            memo[idx] = max(memo[idx], solve(dr, dc) + 1)
    
    return memo[idx]

direction_x = [-1, 1, 0 ,0]
direction_y = [0, 0, 1, -1]
memo = {}
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
for r in range(n):
    for c in range(n):
        answer = max(answer, solve(r, c))

print(answer)
