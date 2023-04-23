import sys
from collections import deque

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        row, col = queue.popleft()

        if (row == row_size - 1 and col == col_size - 1):
            break
        
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
maze = [list(map(int, list(input()))) for _ in range(row_size)]
visited = [[False] * col_size for _ in range(row_size)]

bfs()
print(maze[row_size-1][col_size-1])