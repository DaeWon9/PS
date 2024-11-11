import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
adj_vertices = defaultdict(list)
indegree = defaultdict(int)
graph = []

for _ in range(N):
    graph.append(input().rstrip())

for row in range(N):
    for col in range(row + 1, N):
        if (graph[row][col] == 'Y' and graph[col][row] == 'Y'):
            continue

        if (graph[row][col] == 'Y'):
            indegree[col] += 1
            adj_vertices[row].append(col)

        if (graph[col][row] == 'Y'):
            indegree[row] += 1
            adj_vertices[col].append(row)

queue = deque()
result = []

for vertex in range(N):
    if (indegree[vertex] == 0):
        queue.append(vertex)
        result.append(vertex)

while queue:
    v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        if (indegree[adj_vertex] == 0):
            queue.append(adj_vertex)
            result.append(adj_vertex)

if (len(result) == N):
    print('YES')
else:
    print('NO')