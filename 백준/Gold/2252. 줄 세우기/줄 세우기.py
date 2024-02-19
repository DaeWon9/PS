import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N, M = map(int, input().split())

adj_vertcies = defaultdict(list)
indegree = defaultdict(int)
queue = deque()

for _ in range(M):
    v1, v2 = map(int, input().split())

    adj_vertcies[v1].append(v2)
    indegree[v2] += 1

for vertex in range(1, N + 1):
    if (indegree[vertex] == 0):
        queue.append(vertex)

while queue:
    v = queue.popleft()

    print(v, end = ' ')

    for adj_vertex in adj_vertcies[v]:
        indegree[adj_vertex] -= 1

        if (indegree[adj_vertex] == 0):
            queue.append(adj_vertex)