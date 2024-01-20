import sys
import heapq
from collections import defaultdict, deque

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

distance_list = [ 2147483647 for _ in range(V + 1)]
adj_vertices = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj_vertices[u].append((v, w))

heap = []
heapq.heappush(heap, (0, K))
distance_list[K] = 0

while heap:
    value, vertex = heapq.heappop(heap)

    if (distance_list[vertex] < value):
        continue
    
    for adj_vertex, weight in adj_vertices[vertex]:
        updated_value = value + weight

        if (distance_list[adj_vertex] > updated_value):
            distance_list[adj_vertex] = updated_value
            heapq.heappush(heap, (updated_value, adj_vertex))
            
for vertex_id in range(1, V+1):
    if (distance_list[vertex_id] == 2147483647):
        print('INF')
    else:
        print(distance_list[vertex_id])