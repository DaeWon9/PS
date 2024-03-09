import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < R and 0 <= dc < C):
        return True
    return False

direction_x = [1, 1, 1] 
direction_y = [-1, 0, 1]

R, C = map(int, input().split())
board = []
visited = [[False for _ in range(C)] for _ in range(R)]
queue = deque()
answer = 0

for _ in range(R):
    board.append(list(input().rstrip()))

for r in range(R):
    queue.appendleft((r, 0))
    visited[r][0] = True

while queue:
    row, col = queue.popleft()

    if (col == C - 1):
        answer += 1
        while queue[0][1] != 0:
            r, c = queue.popleft()
            visited[r][c] = False
        continue

    for i in range(3):
        dr = row + direction_y[i]
        dc = col + direction_x[i]

        if (is_movable(dr, dc) and board[dr][dc] == '.' and not visited[dr][dc]):
            queue.appendleft((dr, dc))
            visited[dr][dc] = True

print(answer)