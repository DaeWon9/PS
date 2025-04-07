import sys
input = sys.stdin.readline

def solve(r, c):
    if (dp[r][c] != -1):
        return dp[r][c]
    
    v = board[r][c]

    if (r == N-1 and c == N-1):
        return 1
    
    dp[r][c] = 0

    if (c + v < N): # right
        dp[r][c] += solve(r, c + v)
    
    if (r + v < N): # bottom
        dp[r][c] += solve(r + v, c)
    
    return dp[r][c]

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[-1 for _ in range(N)] for _ in range(N)]

solve(0, 0)
print(dp[0][0])