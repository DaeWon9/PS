import sys
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[2147483647 for _ in range(V + 1)] for _ in range(V + 1)]
adj_vertices = defaultdict(list)

for _ in range(E):
    v1, v2, length = map(int, input().split())
    graph[v1][v2] = length
    adj_vertices[v1].append((v2, length))

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 2147483647
for v in range(1, V + 1):
    if (graph[v][v] != 2147483647):
        answer = min(answer, graph[v][v])

if (answer == 2147483647):
    print(-1)
else:
    print(answer)