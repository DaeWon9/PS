import sys
from collections import defaultdict
import heapq

def dijkstra(start_vertex):
    distance_list = [2147483647 for _ in range(n + 1)] 
    min_heap = []

    heapq.heappush(min_heap, [start_vertex, 0])
    distance_list[start_vertex] = 0

    while min_heap:
        vertex, value = heapq.heappop(min_heap) 

        for v in adj_vertices[vertex]:
            new_distacne = value + graph[vertex][v]

            if new_distacne < distance_list[v]:
                distance_list[v] = new_distacne
                heapq.heappush(min_heap, [v, new_distacne])

    return distance_list

n, e = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
adj_vertices = defaultdict(list)

for _ in range(e):
    v1, v2, d = map(int, sys.stdin.readline().split())
    adj_vertices[v1].append(v2)
    adj_vertices[v2].append(v1)
    graph[v1][v2] = d
    graph[v2][v1] = d

via_vertex_1, via_vertex_2 = map(int, sys.stdin.readline().split())

dijkstra_result = dijkstra(1)
dijkstra_result_via_1 = dijkstra(via_vertex_1)
dijkstra_result_via_2 = dijkstra(via_vertex_2)

# case 1 : 1 -> via_vertex_1 -> via_vertex_2 -> n
case_1 = -1
if (dijkstra_result[via_vertex_1] != 2147483647 and dijkstra_result_via_1[via_vertex_2] != 2147483647 and dijkstra_result_via_2[n] != 2147483647):
    case_1 = dijkstra_result[via_vertex_1] + dijkstra_result_via_1[via_vertex_2] + dijkstra_result_via_2[n]

# case 2 : 1 -> via_vertex_2 -> via_vertex_1 -> n
case_2 = -1
if (dijkstra_result[via_vertex_2] != 2147483647 and dijkstra_result_via_2[via_vertex_1] != 2147483647 and dijkstra_result_via_1[n] != 2147483647):
    case_2 = dijkstra_result[via_vertex_2] + dijkstra_result_via_2[via_vertex_1] + dijkstra_result_via_1[n]

if (case_1 == -1 and case_2 == -1):
    print(-1)
elif (case_1 == -1):
    print(case_2)
elif (case_2 == -1):
    print(case_1)
else:
    print(min(case_1, case_2))
