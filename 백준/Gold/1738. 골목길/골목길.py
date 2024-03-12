import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def is_reachable(start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)

    while queue:
        v = queue.popleft()

        if (v == end):
            return True

        for adj_vertex in adj_vertices[v]:
            if (adj_vertex not in visited):
                queue.append(adj_vertex)
                visited.add(adj_vertex)
    
    return False

n, m = map(int, input().split())
edges = []
assets = [-2147483647 for _ in range(n + 1)]
assets[1] = 0
cycle_vertex_set = set()
prev_vertex = [0 for _ in range(n + 1)]
adj_vertices = defaultdict(list)

for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))
    adj_vertices[start].append(end)

for count in range(n):
    for start, end, cost in edges:
        if (assets[start] != -2147483647 and assets[end] < assets[start] + cost):
            if (count == n - 1):
                cycle_vertex_set.add(start)
                cycle_vertex_set.add(end)

            prev_vertex[end] = start
            assets[end] = assets[start] + cost

route = deque()
route_count = 0
current_vertex = n
route.append(n)

while (current_vertex != 1 and route_count < n):
    route.append(prev_vertex[current_vertex])
    current_vertex = prev_vertex[current_vertex]
    route_count += 1

for vertex in cycle_vertex_set:
    if (is_reachable(vertex, n)):
        print(-1)
        exit(0)

if (is_reachable(1, n)):
    while route:
        print(route.pop(), end = ' ')
else:
    print(-1)