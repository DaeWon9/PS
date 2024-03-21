import sys
input = sys.stdin.readline

answer = 0
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

path_status = [[True for _ in range(N)] for _ in range(N)]

# 역 플로이드
for k in range(N):
    for i in range(N):
        if (i == k):
            continue
        for j in range(N):
            if (i == j or k == j):
                continue
  
            if (board[i][j] == board[i][k] + board[k][j]):
                path_status[i][j] = False
            elif (board[i][j] > board[i][k] + board[k][j]):
                print(-1)
                exit(0)

for i in range(N):
    for j in range(i, N): # 상삼각 행렬만
        if (path_status[i][j]):
            answer += board[i][j]

print(answer)