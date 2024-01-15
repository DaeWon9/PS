import sys
from collections import deque

def is_movable(dr, dc):
    if 0 <= dr < row_size and 0 <= dc < col_size:
        return True
    return False

def bfs(target_pos_x, target_pos_y):
    global use_gram, gram_pos_x, gram_pos_y
    queue = deque()
    queue.append((0, 0, 0)) # row, col, time
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    visited[0][0] = True

    while queue:
        row, col, time = queue.popleft()

        if (row == target_pos_y and col == target_pos_x):
            return time

        for index in range(4):
            dr = row + direction_y[index]
            dc = col + direction_x[index]

            if (is_movable(dr, dc) and graph[dr][dc] != 1 and not visited[dr][dc]):
                if (graph[dr][dc] == 2): # get gram
                    use_gram = time + 1
                    gram_pos_x = dc
                    gram_pos_y = dr
                visited[dr][dc] = True
                queue.append((dr, dc, time + 1))

    return 2147483647

direction_x = [0, 0, 1, -1]
direction_y = [-1, 1, 0, 0]

row_size, col_size, time_limit = map(int, sys.stdin.readline().split())

graph = []

for row_index in range(row_size):
    graph.append(list(map(int, sys.stdin.readline().split())))

gram_pos_x = 0
gram_pos_y = 0
use_gram = 2147483647
not_use_gram = bfs(col_size - 1, row_size - 1)

if (use_gram != 2147483647):
    use_gram += row_size + col_size - 2 - gram_pos_y - gram_pos_x

result = min(not_use_gram, use_gram)

if (result <= time_limit):
    print(result)
else:
    print("Fail")