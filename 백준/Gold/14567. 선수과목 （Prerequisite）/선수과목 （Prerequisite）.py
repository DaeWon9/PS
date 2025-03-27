import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
adj_vertices = defaultdict(list)
indegree = defaultdict(int)
queue = deque()
answer = [0] * N

for _ in range(M):
    u, v = map(int, input().split())

    adj_vertices[u].append(v)
    indegree[v] += 1

for id in range(1, N+1):
    if (indegree[id] == 0):
        queue.append((id, 1))

while queue:
    vertex_id, group_id = queue.popleft()
    answer[vertex_id-1] = group_id

    for adj_vertex in adj_vertices[vertex_id]:
        indegree[adj_vertex] -= 1

        if (indegree[adj_vertex] == 0):
            queue.append((adj_vertex, group_id + 1))

print(*answer)