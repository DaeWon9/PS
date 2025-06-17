import sys
import heapq
input = sys.stdin.readline

# 준호가 집(1번 건물)에서 출발하여 도달할 수 있는 가장 싼 식당과 카페를 들른 후, 
# 다시 집으로 돌아오는 최소 거리를 구해보자.
# 각각의 가격은 모두 다르다.

def solve(start, end):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, v = heapq.heappop(heap)

        if (v == end):
            return d
        
        if (dist[v] < d):
            continue

        for adj_vertex, weight in adj_vertices[v]:
            new_dist = d + weight

            if (dist[adj_vertex] > new_dist):
                dist[adj_vertex] = new_dist
                heapq.heappush(heap, (new_dist, adj_vertex))

N, M = map(int, input().split())
restaurants = [0] + list(map(int, input().split()))
cafes = [0] + list(map(int, input().split()))

for i in range(N+1):
    if (restaurants[i] == 0):
        restaurants[i] = float('inf')

    if (cafes[i] == 0):
        cafes[i] = float('inf')

adj_vertices = [set() for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())

    adj_vertices[u].add((v, w))
    adj_vertices[v].add((u, w))

default_dist = [float('inf') for _ in range(N+1)]
default_dist[1] = 0
heap = [(0, 1)]

while heap:
    d, v = heapq.heappop(heap)
    
    if (default_dist[v] < d):
        continue

    for adj_vertex, weight in adj_vertices[v]:
        new_dist = d + weight

        if (default_dist[adj_vertex] > new_dist):
            default_dist[adj_vertex] = new_dist
            heapq.heappush(heap, (new_dist, adj_vertex))

cafe_min = float('inf')
target_cafe = 1

restaurant_min = float('inf')
target_restaurant = 1

for idx in range(2, N+1):
    if (default_dist[idx] == float('inf')):
        continue

    if (cafe_min > cafes[idx]):
        target_cafe = idx
        cafe_min = cafes[idx]

    if (restaurant_min > restaurants[idx]):
        target_restaurant = idx
        restaurant_min = restaurants[idx]

print(default_dist[target_restaurant] + default_dist[target_cafe] + solve(target_cafe, target_restaurant))
