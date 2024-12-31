import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    return (0 <= dr < H and 0 <= dc < W)

direction_x = [1, 0, 0, -1]
direction_y = [0, 1, -1 ,0]
h_direction_x = [1, 2, 2, 1, -1, -2, -2, -1]
h_direction_y = [-2, -1, 1, 2, 2, 1, -1, -2]

K = int(input())
W, H = map(int, input().split())
board = []
distance = [[[2147483647 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]
queue = deque()

for _ in range(H):
    board.append(list(map(int, input().split())))

if (W == 1 and H == 1):
    print(0)
    exit(0)

queue.append((0, 0, 0, 0)) # k, m, r, c

while queue:
    k, m, r, c = queue.popleft()

    if (k+1 <= K):
        for i in range(8):
            dr = r + h_direction_y[i]
            dc = c + h_direction_x[i]

            if (is_movable(dr, dc) and board[dr][dc] == 0):
                if (distance[k+1][dr][dc] > m+1):
                    distance[k+1][dr][dc] = m+1
                    queue.append((k+1, m+1, dr, dc))
    
    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc) and board[dr][dc] == 0):
            if (distance[k][dr][dc] > m+1):
                distance[k][dr][dc] = m+1
                queue.append((k, m+1, dr, dc))

answer = 2147483647
for i in range(K+1):
    if (answer > distance[i][-1][-1]):
        answer = distance[i][-1][-1]

if (answer == 2147483647):
    print(-1)
else:
    print(answer)