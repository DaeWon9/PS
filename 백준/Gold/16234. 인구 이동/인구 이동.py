import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(row, col):
    area_queue = deque([(row, col)])
    visit[row][col] = True

    union = [(row, col)]
    union_people_sum = area[row][col]
    
    while area_queue:
        x, y = area_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < N and 0 <= ny < N and not visit[nx][ny]) and (L <= abs(area[nx][ny] - area[x][y]) <= R):
                union.append((nx, ny))
                visit[nx][ny] = True
                area_queue.append((nx, ny))
                union_people_sum += area[nx][ny]

    for x, y in union:
        area[x][y] = int(union_people_sum / len(union))

    return(len(union))

N, L, R = map(int, sys.stdin.readline().split()) 
area = []
a_list = []

for i in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))

day = 0    
while (True):  
    result_list = []
    visit = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not visit[row][col]:
                result_list.append(bfs(row, col))

    if (max(result_list) == 1):
        break

    day += 1

print(day)