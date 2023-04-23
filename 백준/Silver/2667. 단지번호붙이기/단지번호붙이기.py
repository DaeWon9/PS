import sys
from collections import deque

def bfs(pos_x, pos_y):
    count = 1
    queue = deque([(pos_x, pos_y)])
    visited[pos_x][pos_y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        row, col = queue.popleft()
        
        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]
            
            if (0 <= x < n and 0 <= y < n and not visited[x][y]):
                if (danzi[x][y] == 1):
                    visited[x][y] = True
                    queue.append([x, y])
                    count += 1
    result.append(count)

n = int(sys.stdin.readline())

danzi = []
danzi = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for row in range(n):
    for col in range(n):
        if (not visited[row][col] and danzi[row][col] == 1):
            bfs(row, col)

result.sort()
print(len(result))
for count in result:
    print(count)