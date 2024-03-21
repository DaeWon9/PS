import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
keys = list(map(str, input().split()))
keys.sort()
M = int(input())

indegree = defaultdict(int)
adj_vertices = defaultdict(list)
children_info = defaultdict(list)
queue = deque()
K = []

for _ in range(M):
    v1, v2 = map(str, input().split()) # v1의 조상중에 v2가 존재 v2 -> v1

    indegree[v1] += 1
    adj_vertices[v2].append(v1)

for key in keys:
    if (indegree[key] == 0):
        queue.append(key)
        K.append(key)

while queue:
    v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        
        if (indegree[adj_vertex] == 0):
            children_info[v].append(adj_vertex)
            queue.append(adj_vertex)

print(len(K))
print(*K)
for key in keys:
    children_info[key].sort()
    print(key, len(children_info[key]), *children_info[key])