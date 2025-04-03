import sys
from collections import defaultdict, deque
input = sys.stdin.readline

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
    
    if (x < y):
        group_size[x] += group_size[y]
        del group_size[y]
        parent[y] = x
    else:
        group_size[y] += group_size[x]
        del group_size[x]
        parent[x] = y


N, M, X = map(int, input().split())
indegree = defaultdict(int)
adj_vertices = defaultdict(list)
level = [0] * (N+1)

parent = [i for i in range(N+1)]
group_size = defaultdict(lambda: 1)

vertices_per_level = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split()) # A가 B보다 더 잘함
    union(A, B)
    adj_vertices[A].append(B)
    indegree[B] += 1

target_group_id = parent[X]
queue = deque()

for id in range(1, N+1):
    if (indegree[id] == 0):
        queue.append((1, id)) # level, vertex
        level[id] = 1

        if (parent[id] == target_group_id):
            vertices_per_level[1].append(id)

while queue:
    l, v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        level[adj_vertex] = max(l+1, level[adj_vertex])

        if (indegree[adj_vertex] == 0):
            queue.append((level[adj_vertex], adj_vertex))

            if (parent[adj_vertex] == target_group_id):
                vertices_per_level[level[adj_vertex]].append(adj_vertex)

min_result = level[X]
max_result = level[X] + (len(vertices_per_level[level[X]])- 1) + (N - group_size[target_group_id])

print(min_result, max_result)