import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

adj_vertices = defaultdict(list)
distance = [2147483647] * (N + 1)
distance[X] = 0

for _ in range(M):
    v1, v2 = map(int, input().split()) # v1 -> v2
    adj_vertices[v1].append(v2)

queue = deque([(0, X)])

while queue:
    dist, v = queue.popleft()

    if (distance[v] < dist):
        continue

    for adj_vertex in adj_vertices[v]:
        updated_dist = dist + 1

        if (distance[adj_vertex] > updated_dist):
            queue.append((updated_dist, adj_vertex))
            distance[adj_vertex] = updated_dist
            
flag = False
for idx, dist in enumerate(distance):
    if (dist == K):
        print(idx)
        flag = True

if (not flag):
    print(-1)
