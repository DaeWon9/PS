import sys
from collections import deque
input = sys.stdin.readline

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

def calc_index(r, c):
    return r * M + c

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < M):
        return True
    return False

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
    
    if (x < y):
        fire_set.add(x)
        if (y in fire_set):
            fire_set.remove(y)
        parent[y] = x
    else:
        fire_set.add(y)
        if (x in fire_set):
            fire_set.remove(x)
        parent[x] = y

def fire_union():
    for r, c in fire_queue:
        current_index = calc_index(r, c)
        for i in range(4):
            dr = r + direction_y[i]
            dc = c + direction_x[i]

            if (is_movable(dr, dc) and visited[dr][dc]): # fire
                next_index = calc_index(dr, dc)
                if (find(current_index) != find(next_index)):
                    union(current_index, next_index)

def spread_fire():
    global fire_count
    for _ in range(len(fire_queue)):
        r, c = fire_queue.popleft()

        for i in range(4):
            dr = r + direction_y[i]
            dc = c + direction_x[i]

            if (is_movable(dr, dc) and not visited[dr][dc]):
                if (board[dr][dc] == '1'):
                    fire_queue.append((dr, dc))
                    visited[dr][dc] = True

N, M = map(int, input().split())
board = []
parent = [i for i in range(N * M)]
visited = [[False for _ in range(M)] for _ in range(N)]

fire_set = set()
fire_count = 0
fire_queue = deque()

for r in range(N):
    input_data = list(map(str, list(str(input().rstrip()))))
    for c in range(M):
        if (input_data[c] == '0'): # 불
            fire_queue.append((r, c))
            visited[r][c] = True
            fire_count += 1
            fire_set.add(calc_index(r, c))
        
    board.append(input_data)

day = 0
temp_day = 0
answer = 2147483647
group_len = 2147483647

while True:
    fire_union()

    if (group_len > len(fire_set)):
        group_len = len(fire_set)
        answer = fire_count
        temp_day = day
    
    if (not fire_queue):
        break

    if (len(fire_set) <= 1):
        print(day, fire_count)
        exit(0)

    spread_fire()

    day += 1
    fire_count += len(fire_queue)

print(temp_day, answer)