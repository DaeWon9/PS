import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < M)

direction_x = [1, 0, 0, -1]
direction_y = [0, 1, -1, 0]

N, M, K = map(int, input().split())
board = []
visited = [[[False for _ in range(M+1)] for _ in range(N+1)] for _ in range(K+1)]

for _ in range(N):
    board.append(input().rstrip())

queue = deque([(0, 0, 0, 0)])
visited[0][0][0] = True

while queue:
    d, b, r, c = queue.popleft()

    if (r == N - 1 and c == M - 1):
        print(d+1)
        exit(0)

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc)):
            if (board[dr][dc] == '1'): # wall
                if (b + 1 <= K and not visited[b+1][dr][dc]):
                    queue.append((d+1, b+1, dr, dc))
                    visited[b+1][dr][dc] = True
            else:
                if (not visited[b][dr][dc]):
                    queue.append((d+1, b, dr, dc))
                    visited[b][dr][dc] = True
print(-1)
