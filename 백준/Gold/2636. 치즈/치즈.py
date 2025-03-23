import sys
from collections import deque
input = sys.stdin.readline

def is_movable(r, c):
    return 0 <= r < N and 0 <= c < M

def is_melted(r, c):
    queue = deque()
    queue.append((r, c))
    visited = set()
    visited.add((r, c))

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            nr = row + direction_y[i]
            nc = col + direction_x[i]

            if (not is_movable(nr, nc)):
                return True

            if (board[nr][nc] == 0 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc))

    return False

N, M = map(int, input().split())
board = []
cheese_pos_set = set()

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

for r in range(N):
    input_data = list(map(int, input().split()))

    for c in range(M):
        data = input_data[c]

        if (data == 1): # cheese
            cheese_pos_set.add((r, c))

    board.append(input_data)

t = 0
remain_count = len(cheese_pos_set)
last_remain_count = len(cheese_pos_set)

while (remain_count > 0):
    last_remain_count = len(cheese_pos_set)
    cheese_queue = deque(cheese_pos_set)
    deleted_cheese_set = set()

    while cheese_queue:
        row, col = cheese_queue.popleft()

        if (is_melted(row, col)):
            deleted_cheese_set.add((row, col))

    for r, c in deleted_cheese_set:
        board[r][c] = 0

    cheese_pos_set = cheese_pos_set - deleted_cheese_set
    remain_count = len(cheese_pos_set)
    t += 1

print(t)
print(last_remain_count)
