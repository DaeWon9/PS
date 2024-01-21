import sys
from collections import defaultdict
import heapq

def solution(start, end):
    distance = [2147483647] * (n + 1)
    heap = []

    distance[start] = 0
    heapq.heappush(heap, (0, start)) # [현재 정점의 가중치, id]

    while heap:
        value, vertex = heapq.heappop(heap)

        if (distance[vertex] < value):
            continue

        for adj_vertex_id, time in adj_vertex_dict[vertex]:
            updated_time = value + time
            
            if (updated_time < distance[adj_vertex_id]):
                distance[adj_vertex_id] = updated_time
                heapq.heappush(heap, (updated_time, adj_vertex_id))
        
    return distance[end]

n, m, x = map(int, sys.stdin.readline().split())
adj_vertex_dict = defaultdict(list)
max_time = 0

for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    adj_vertex_dict[start].append([end, time])

for village_id in range(1, n+1):
    if (village_id == x):
        continue

    result_time = solution(village_id, x) + solution(x, village_id)
    
    if (result_time > max_time):
        max_time = result_time
    
print(max_time)