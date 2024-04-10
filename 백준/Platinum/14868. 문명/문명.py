import sys
from collections import deque
input = sys.stdin.readline

def calc_index(r, c):
    return r * N + c

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < N):
        return True
    return False

def union_civilization():
    for r, c in queue:
        target_index = calc_index(r, c)

        for i in range(4):
            dr = r + direction_r[i]
            dc = c + direction_c[i]

            if (is_movable(dr, dc) and visited[dr][dc]): # 문명
                moved_index = calc_index(dr, dc)

                if (find(target_index) != find(moved_index)):
                    union(target_index, moved_index)

def spread_civilization():
    for _ in range(len(queue)):
        r, c = queue.popleft()

        for i in range(4):
            dr = r + direction_r[i]
            dc = c + direction_c[i]

            if (is_movable(dr, dc) and not visited[dr][dc]):
                visited[dr][dc] = True
                queue.append((dr, dc))

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
        group_set.add(x)
        if (y in group_set):
            group_set.remove(y)
        parent[y] = x
    else:
        group_set.add(y)
        if (x in group_set):
            group_set.remove(x)
        parent[x] = y

direction_r = [0, 0, 1, -1]
direction_c = [1, -1, 0, 0]

N, K = map(int, input().split())
board = [[(N * r) + c for c in range(N)] for r in range(N)]
parent = [i for i in range(N * N)]
visited = [[False for _ in range(N)] for _ in range(N)]
group_set = set()
queue = deque()

for _ in range(K):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    visited[r][c] = True
    queue.append((r, c))
    group_set.add(calc_index(r, c))

year = 0

while True:
    union_civilization()
    
    if (len(group_set) == 1):
        break

    spread_civilization()

    year += 1

print(year)