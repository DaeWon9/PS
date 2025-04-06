import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def set_node_idx(v):
    global idx
    l, r = child_list[v]
    visited[v] = True

    if (l != -1 and not visited[l]):
        set_node_idx(l)

    result[v] = idx
    idx += 1
    
    if (r != -1 and not visited[r]):
        set_node_idx(r)

N = int(input())
child_list = defaultdict(tuple)
result = [0] * (N+1)
indegree = [0] * (N+1)

idx = 0

min_max_dict = defaultdict(lambda: [10001, 0]) # min, max

for _ in range(N):
    v, l, r = map(int, input().split())
    if (l != -1):
        indegree[l] += 1
    if (r != -1):
        indegree[r] += 1
    child_list[v] = (l, r)

root = 0
for i in range(1, N+1):
    if (indegree[i] == 0):
        root = i

visited = [False] * (N+1)
visited[root] = True

set_node_idx(root)

queue = deque()
queue.append((1, root)) # level, vertex

max_level = 0
max_width = 0

while queue:
    l, v = queue.popleft()
    vertex_idx = result[v]

    min_max_dict[l][0] = min(min_max_dict[l][0], vertex_idx)
    min_max_dict[l][1] = max(min_max_dict[l][1], vertex_idx)
    width = min_max_dict[l][1] - min_max_dict[l][0] + 1

    if (width > max_width):
        max_width = width
        max_level = l

    for child in child_list[v]:
        if (child == -1):
            continue

        queue.append((l+1, child))

print(max_level, max_width)