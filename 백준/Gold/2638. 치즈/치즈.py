import sys
from collections import deque
input = sys.stdin.readline

def is_melting_cheese(r, c):
    count = 0
    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (not is_movable(dr, dc)):
            count += 1
            continue
    
        if (board[dr][dc] == 1):
            continue

        if (is_out_border(dr, dc)):
            count += 1
    
    return (count >= 2)

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < M)

def is_out_border(r, c):
    visited_set = set()
    queue = deque()
    queue.append((r, c))
    visited_set.add((r, c))

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            dr = row + direction_y[i]
            dc = col + direction_x[i]

            if (not is_movable(dr, dc)):
                return True

            if (board[dr][dc] == 1):
                continue

            if ((dr, dc) in visited_set):
                continue

            queue.append((dr, dc))
            visited_set.add((dr, dc))

    return False


direction_x = [1, 0, 0, -1]
direction_y = [0, -1, 1, 0]

N, M = map(int, input().split())
board = []
cheese_queue = deque()

for row in range(N):
    input_data = list(map(int, input().split()))
    for col, data in enumerate(input_data):
        if (data == 1): # 치즈
            cheese_queue.append((row, col))
    
    board.append(input_data)

answer = 0
while cheese_queue:
    melting_cheese_set = set()
    for _ in range(len(cheese_queue)):
        r, c = cheese_queue.popleft()

        if (is_melting_cheese(r, c)):
            melting_cheese_set.add((r, c))
        else:
            cheese_queue.append((r, c))
    
    for cr, cc in melting_cheese_set:
        board[cr][cc] = 0
    
    answer += 1

print(answer)