import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[2147483647 for _ in range(n + 1)] for _ in range(n + 1)]
adj_vertices = defaultdict(list)

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    if (graph[v1][v2] > cost):
        adj_vertices[v1].append(v2)
        graph[v1][v2] = cost

start_v, end_v = map(int, input().split())
distance_list = [2147483647 for _ in range(n + 1)]
distance_list[start_v] = 0
heap = [(0, start_v)]
prev_vertex = defaultdict(int)

while heap:
    cost, v = heapq.heappop(heap)

    if (v == end_v):
        break

    if (cost > distance_list[v]):
        continue

    for vertex in adj_vertices[v]:
        if (cost + graph[v][vertex] < distance_list[vertex]):
            distance_list[vertex] = cost + graph[v][vertex]
            prev_vertex[vertex] = v
            heapq.heappush(heap, (cost + graph[v][vertex], vertex))


result_road = [end_v]
current_v = end_v

while start_v != current_v:
    current_v = prev_vertex[current_v]
    result_road.append(current_v)

result_road.reverse()

print(distance_list[end_v])
print(len(result_road))
for v in result_road:
    print(v, end=' ')