import sys
from collections import deque
input = sys.stdin.readline

def find(x):
    if (parent[x] == x):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return
    elif x < y:
        parent[y] = x
    else:
        parent[x] = y

def water_union():
    for r, c in queue:
        for i in range(4):
            dr = r + direction_y[i]
            dc = c + direction_x[i]

            if (is_movable(dr, dc) and visited[dr][dc]): # water
                union(board_id[dr][dc], board_id[r][c])

def melt():
    for _ in range(len(queue)):
        r, c = queue.popleft()

        for i in range(4):
            dr = r + direction_y[i]
            dc = c + direction_x[i]

            if (is_movable(dr, dc) and not visited[dr][dc]):
                queue.append((dr, dc))
                visited[dr][dc] = True

def is_movable(dr, dc):
    if (0 <= dr < R and 0 <= dc < C):
        return True
    return False

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

R, C = map(int, input().split())
board = []
swan_pos = []
queue = deque()
visited = [[False for _ in range(C)] for _ in range(R)]

for r in range(R):
    input_data = list(input().rstrip())

    for c in range(C):
        if (input_data[c] == 'L'):
            swan_pos.append((r, c))
            queue.append((r, c))
            input_data[c] = '.'
            visited[r][c] = True
        elif (input_data[c] == '.'):
            queue.append((r, c))
            visited[r][c] = True

    board.append(input_data)

parent = [i for i in range(R * C)]
board_id = [[i for i in range(C * r, C * (r + 1))] for r in range(R)]
day = 0

while True:
    water_union()
    if (find(board_id[swan_pos[0][0]][swan_pos[0][1]]) == find(board_id[swan_pos[1][0]][swan_pos[1][1]])):
        break
    melt()
    day += 1

print(day)