import sys
from collections import deque

def is_movable(dr, dc):
    if (0 <= dr < row_size and 0 <= dc < col_size):
        return True
    return False

def is_peak_possible(row, col, value):    
    for index in range(8): # 8방향
        dr = row + direction_y[index]
        dc = col + direction_x[index]

        if (is_movable(dr, dc) and graph[dr][dc] > value):
            return False
    return True

def get_target_peak():
    for row in range(last_target_peak_pos[0], row_size):
        if (row == last_target_peak_pos[0]):
            for col in range(last_target_peak_pos[1], col_size):
                if (visited[row][col] == False):
                    return [row, col]
        else:
            for col in range(col_size):
                if (visited[row][col] == False):
                    return [row, col]
    return [-1, -1]

direction_x = [0, -1, -1, -1, 0, 1, 1, 1]  # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
direction_y = [-1, -1, 0, 1, 1, 1, 0, -1]

row_size, col_size = map(int, sys.stdin.readline().split())

graph = []

for _ in range(row_size):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[False for _ in range(col_size)] for _ in range(row_size)]

queue = deque()
last_target_peak_pos = [0, 0]

answer = 0

while True:
    target_peak_row, target_peak_col = get_target_peak()
    target_peak_value = graph[target_peak_row][target_peak_col]

    if (target_peak_row == -1): # finish
        break

    queue.append((target_peak_row, target_peak_col, target_peak_value))
    visited[target_peak_row][target_peak_col] = True

    is_peak = True

    while queue:
        row, col, value = queue.popleft()

        if (not is_peak_possible(row, col, value)):
            is_peak = False

        for index in range(8): # 8방향
            dr = row + direction_y[index]
            dc = col + direction_x[index]

            if (is_movable(dr, dc) and not visited[dr][dc] and graph[dr][dc] == value):
                visited[dr][dc] = True
                queue.append((dr, dc, graph[dr][dc]))

    if (is_peak):
        answer += 1

print(answer)