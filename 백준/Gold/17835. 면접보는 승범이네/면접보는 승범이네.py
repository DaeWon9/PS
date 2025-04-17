import sys
import heapq
input = sys.stdin.readline

INF = float("inf")
N, M, K = map(int, input().split())

reversed_graph = [[] for _ in range(N+1)]
heap = []
distance = [INF] * (N+1)

for _ in range(M):
    u, v, c = map(int, input().split())
    reversed_graph[v].append((u, c))

for interview_room in list(map(int, input().split())):
    heapq.heappush(heap, (0, interview_room))
    distance[interview_room] = 0

while heap:
    d, v = heapq.heappop(heap)

    if (distance[v] < d):
        continue

    for adj_vertex, cost in reversed_graph[v]:
        new_distane = d + cost

        if (distance[adj_vertex] > new_distane):
            distance[adj_vertex] = new_distane
            heapq.heappush(heap, (new_distane, adj_vertex))

max_vertex = 0
max_distance = 0
for v in range(1, N+1):
    if (max_distance < distance[v]):
        max_distance = distance[v]
        max_vertex = v

print(max_vertex)
print(max_distance)
