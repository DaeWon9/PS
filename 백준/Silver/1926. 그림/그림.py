import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def is_movable(dr, dc):
    return (0 <= dr < n and 0 <= dc < m)

def find(x):
    if (x == parent[x]):
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global max_count
    x = find(x)
    y = find(y)

    if (x == y):
        return
    
    if (x < y):
        count_dict[x] += count_dict[y]
        count_dict[y] = 0
        parent[y] = x
        picture_set.add(x)
        picture_set.discard(y)
        max_count = max(max_count, count_dict[x])
    else:
        count_dict[y] += count_dict[x]
        count_dict[x] = 0
        parent[x] = y
        picture_set.add(y)
        picture_set.discard(x)
        max_count = max(max_count, count_dict[y])

def get_index(r, c):
    return r * m + c

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]
n, m = map(int, input().split())
board = []
queue = deque()
picture_set = set()
visited = [[False for _ in range(m)] for _ in range(n)]
count_dict = defaultdict(int)
max_count = 0

for r in range(n):
    input_data = list(map(int, input().split()))
    for c, data in enumerate(input_data):
        if (data == 1):
            queue.append((r, c))
            cur_idx = get_index(r, c)
            picture_set.add(cur_idx)
            count_dict[cur_idx] = 1
            max_count = 1
    board.append(input_data)

parent = [i for i in range(n * m)]

while queue:
    r, c = queue.popleft()
    cur_idx = get_index(r, c)

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc) and not visited[dr][dc] and board[dr][dc] == 1):
            next_idx = get_index(dr, dc)
            if (find(cur_idx) != find(next_idx)):
                union(cur_idx, next_idx)

print(len(picture_set))
print(max_count)