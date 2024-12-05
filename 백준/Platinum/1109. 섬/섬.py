import sys
from collections import deque, defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < M)

def get_pos(idx):
    return (idx // M, idx % M)

def get_idx(row, col):
    return row * M + col

def dfs(r, c, idx):
    if (visited[r][c]):
        return

    visited[r][c] = True
    group_idx_set.add(idx)

    for i in range(8):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (not is_movable(dr, dc)):
            root_set.add(idx)
            continue

        target_group_idx = get_idx(dr, dc)
        if (board[dr][dc] == 'x' and not visited[dr][dc]):
            group[target_group_idx] = idx
            dfs(dr, dc, idx)

def find_parent_group_idx(group_idx):
    count_dict = defaultdict(int)
    row, col = get_pos(group_idx)
    visited_set = set()
    q = deque()

    visited_set.add((row, col))
    q.append((row, col))

    while q:
        r, c = q.popleft()

        for i in range(4):
            dr = r + direction_y[i]
            dc = c + direction_x[i]

            idx = get_idx(dr, dc)

            if (not is_movable(dr, dc)):
                return group_idx

            if ((dr, dc) in visited_set):
                continue

            if (group[idx] == group_idx):
                continue

            if (group[idx] != -1):
                count_dict[group[idx]] += 1
            else:
                q.append((dr, dc))

            visited_set.add((dr, dc))

    parent_group_idx = -1
    max_count = 0

    for key in count_dict.keys():
        if (count_dict[key] > max_count):
            parent_group_idx = key
            max_count = count_dict[key]
    
    return parent_group_idx

N, M = map(int, input().split())
H = min(N, M) + 1
answer = [0] * H
visited = [[False for _ in range(M)] for _ in range(N)]
board = []
group = [i for i in range(N * M)]
group_idx_set = set()
queue = deque()

root_set = set()
indegree = defaultdict(int)
adj_vertices = defaultdict(list)
height_dict = defaultdict(int)

direction_x = [0, 0, 1, -1, 1, -1, 1, -1]
direction_y = [1, -1, 0, 0, 1, 1, -1, -1]

for row in range(N):
    input_data = input().rstrip()

    for col in range(M):
        if (input_data[col] == 'x'):
            queue.append((row, col))
        else:
            idx = get_idx(row, col)
            group[idx] = -1

    board.append(input_data)

if (not queue):
    print(-1) 
    exit(0)

while queue:
    r, c = queue.popleft()
    dfs(r, c, get_idx(r, c))

for group_idx in group_idx_set:
    if (group_idx in root_set):
        continue

    parent_group_idx = find_parent_group_idx(group_idx)
    if (group_idx == parent_group_idx or parent_group_idx == -1):
        continue

    adj_vertices[group_idx].append(parent_group_idx)
    indegree[parent_group_idx] += 1

for group_idx in group_idx_set:
    if (indegree[group_idx] == 0):
        queue.append((0, group_idx))
        height_dict[group_idx] = 0

while queue:
    level, v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        height_dict[adj_vertex] = max(level + 1, height_dict[adj_vertex])
        
        if (indegree[adj_vertex] == 0):
            queue.append((level + 1, adj_vertex))

for value in height_dict.values():
    answer[value] += 1

for ans in answer:
    if (ans == 0): 
        break
    print(ans, end=' ')