import sys
from collections import deque

def bfs(target):
    queue = deque(target)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]
            
            if (0 <= x < row_size and 0 <= y < col_size and not visited[x][y]):
                if (maze[x][y] == 1):
                    visited[x][y] = True
                    queue.append([x, y])
                    maze[x][y] = maze[row][col] + 1 

row_size, col_size = map(int, sys.stdin.readline().rstrip().split())

maze = []
for _ in range(row_size):
    maze.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[False] * col_size for _ in range(row_size)]

target = [(i,j) for i in range(row_size) for j in range(col_size) if maze[i][j]==2]

bfs(target)

for row in maze:
    for data in row:
        if (data != 0):
            print(data - 2, end = " ")
        else:
            print(data, end = " ")
    print()