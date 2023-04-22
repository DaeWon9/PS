import sys
from collections import deque

def explode_bombs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while bomb_queue:
        a, b = bomb_queue.popleft()
        graph[a][b] = "."

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if (0 <= x < row_count and 0 <= y < col_count):
                if graph[x][y] == "O":
                    graph[x][y] = "."

row_count, col_count, time = map(int, sys.stdin.readline().split())
graph = []
for _ in range(row_count):
    graph.append(list(map(str, sys.stdin.readline().strip())))

time -= 1
while time:
    bomb_queue = deque()

    for row in range(row_count):
        for col in range(col_count):
            if graph[row][col] == 'O':
                bomb_queue.append((row, col))

    for row in range(row_count):
        for col in range(col_count):
            if graph[row][col] == ".":
                graph[row][col] = "O"

    time -= 1
    if time == 0:
        break

    explode_bombs()
    time -= 1

for i in graph:
    print("".join(i))