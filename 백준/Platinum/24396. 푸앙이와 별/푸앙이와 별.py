import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
removed_edge_dict = defaultdict(set)

for _ in range(M):
    v1, v2 = map(int, input().split())
    removed_edge_dict[v1].add(v2)
    removed_edge_dict[v2].add(v1)

queue = deque([1]) #vertex
distance = [0] * (N + 1)
dist = 0

while queue:
    removed_status = [0] * (N + 1)
    size = len(queue)

    for _ in range(size):
        v = queue.popleft()
        distance[v] = dist

        for removed_edge in removed_edge_dict[v]:
            removed_status[removed_edge] += 1

    for vertex in range(2, N + 1):
        if (removed_status[vertex] != size and distance[vertex] == 0):
            queue.append(vertex)
    
    dist += 1

print(0)
for dist in distance[2:]:
    if (dist == 0):
        print(-1)
    else:
        print(dist)