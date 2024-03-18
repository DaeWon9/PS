import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
adj_vertices = defaultdict(list)
heap = []
distance = [2147483647 for _ in range(N + 1)]
prev_vertex = defaultdict(int)

for _ in range(M):
    v1, v2, time = map(int, input().split())
    adj_vertices[v1].append((v2, time))
    adj_vertices[v2].append((v1, time))


distance[1] = 0 # 1번이 슈퍼컴퓨터
heap = [[0, 1]]

while heap:
    value, vertex = heapq.heappop(heap)

    if (distance[vertex] < value):
        continue

    for adj_vertex, connected_value in adj_vertices[vertex]:
        if (distance[adj_vertex] > value + connected_value):
            distance[adj_vertex] = value + connected_value
            prev_vertex[adj_vertex] = vertex

            heapq.heappush(heap, (value + connected_value, adj_vertex))

print(N - 1)
for key in prev_vertex.keys():
    print(prev_vertex[key], key)