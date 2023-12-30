import sys
from collections import deque

def solve(x,y,z):
    queue = deque()
    queue.append((x,y,z))

    while queue:
        x, y, c = queue.popleft()
        if x == n - 1 and y == m - 1: # finish
            return visited[x][y][c]
        
        for i in range(4):
            dx = x + direction_x[i]
            dy = y + direction_y[i]

            if dx < 0 or dx >= n or dy < 0 or dy >= m: # not movable
                continue

            if graph[dx][dy] == 1 and c == 0:
                visited[dx][dy][1] = visited[x][y][0] + 1
                queue.append((dx, dy, 1))
            elif graph[dx][dy] == 0 and visited[dx][dy][c] == 0:
                visited[dx][dy][c] = visited[x][y][c] + 1
                queue.append((dx, dy, c))
    return -1
                            
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

direction_x = [-1,0,1,0]
direction_y =[0,1,0,-1]

print(solve(0,0,0))