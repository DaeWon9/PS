import sys
from collections import defaultdict
input = sys.stdin.readline

# 서: 1, 북: 2, 동: 4, 남: 8
W = 1
N = 2
E = 4
S = 8

COLS, ROWS = map(int, input().split())  # 열 개수, 행 개수
parent = [i for i in range(COLS * ROWS)]
group_id_set = set(range(COLS * ROWS))
group_size = defaultdict(lambda: 1)
disconnected_group = defaultdict(set)

def is_in(r, c):
    return (0 <= r < ROWS) and (0 <= c < COLS)

def get_idx(r, c):
    return (r * COLS) + c

def find(x):
    if (x == parent[x]):
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return
    
    disconnected_group[x].discard(y)
    disconnected_group[y].discard(x)
    
    if (x < y):
        group_id_set.discard(y)
        group_size[x] += group_size[y]
        parent[y] = x
    else:
        group_id_set.discard(x)
        group_size[y] += group_size[x]
        parent[x] = y

for r in range(ROWS):
    input_data = list(map(int, input().split()))
    for c, data in enumerate(input_data):
        pivot_idx = get_idx(r, c)
        
        if (is_in(r, c-1)):
            cur_idx = get_idx(r, c-1)
            if ((data & W) == 0):
                union(pivot_idx, cur_idx)
            else:
                parent_pivot_idx = find(pivot_idx)
                parent_cur_idx = find(cur_idx)
                if (parent_pivot_idx != parent_cur_idx):
                    disconnected_group[parent_pivot_idx].add(parent_cur_idx)
                    disconnected_group[parent_cur_idx].add(parent_pivot_idx)
        
        if (is_in(r-1, c)):
            cur_idx = get_idx(r-1, c)
            if ((data & N) == 0):
                union(pivot_idx, cur_idx)
            else:
                parent_pivot_idx = find(pivot_idx)
                parent_cur_idx = find(cur_idx)
                if (parent_pivot_idx != parent_cur_idx):
                    disconnected_group[parent_pivot_idx].add(parent_cur_idx)
                    disconnected_group[parent_cur_idx].add(parent_pivot_idx)
        
        if (is_in(r, c+1)):
            cur_idx = get_idx(r, c+1)
            if ((data & E) == 0):
                union(pivot_idx, cur_idx)
            else:
                parent_pivot_idx = find(pivot_idx)
                parent_cur_idx = find(cur_idx)
                if (parent_pivot_idx != parent_cur_idx):
                    disconnected_group[parent_pivot_idx].add(parent_cur_idx)
                    disconnected_group[parent_cur_idx].add(parent_pivot_idx)
        
        if (is_in(r+1, c)):
            cur_idx = get_idx(r+1, c)
            if ((data & S) == 0):
                union(pivot_idx, cur_idx)
            else:
                parent_pivot_idx = find(pivot_idx)
                parent_cur_idx = find(cur_idx)
                if (parent_pivot_idx != parent_cur_idx):
                    disconnected_group[parent_pivot_idx].add(parent_cur_idx)
                    disconnected_group[parent_cur_idx].add(parent_pivot_idx)

max_size = 0
max_unioned_size = 0
for id in group_id_set:
    target_size = group_size[id]
    max_size = max(max_size, target_size)
    
    disconnected_group_set = set()
    for x in disconnected_group[id]:
        px = find(x)
        if (px != id):
            disconnected_group_set.add(px)
    
    for v in disconnected_group_set:
        max_unioned_size = max(max_unioned_size, target_size + group_size[v])

print(len(group_id_set))
print(max_size)
print(max_unioned_size)
