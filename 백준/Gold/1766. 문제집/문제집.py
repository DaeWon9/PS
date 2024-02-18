import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
adj_vertices = defaultdict(list)
indegree = defaultdict(int)

heap = []

for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_vertices[v1].append(v2)
    indegree[v2] += 1

for vertex in range(1, N + 1):
    if (indegree[vertex] == 0):
        heapq.heappush(heap, vertex)

while heap:
    v = heapq.heappop(heap)

    print(v, end = ' ')

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        
        if (indegree[adj_vertex] == 0):
            heapq.heappush(heap, adj_vertex)