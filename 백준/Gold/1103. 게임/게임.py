import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def is_movable(r, c):
    return (0 <= r < N and 0 <= c < M)

def dfs(r, c):
    if (dp[r][c] != -1):
        return dp[r][c]
    
    visited[r][c] = True
    
    dp[r][c] = 1
    x = int(board[r][c])
    
    for i in range(4):
        nr = r + dr[i] * x
        nc = c + dc[i] * x
        
        if (not is_movable(nr, nc) or board[nr][nc] == 'H'):
            continue
            
        if (visited[nr][nc]):
            print(-1)
            exit(0)
            
        dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    
    visited[r][c] = False
    return dp[r][c]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(input().rstrip())

dp = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

print(dfs(0, 0))