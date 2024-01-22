import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def is_reachable(cycle_vertices, e):
    queue = deque()
    for vertex in cycle_vertices:
        queue.append(vertex)
    visited = [False] * n

    while queue:
        start_vertex = queue.popleft()

        for adj_vertex in adj_vertices[start_vertex]:
            if (not visited[adj_vertex]):
                if (adj_vertex == e):
                    return True
                queue.append(adj_vertex)      
                visited[adj_vertex] = True

    return False 

def solution():    
    is_has_plus_cycle = False
    cycle_vertices = []

    for count in range(n):
        for start, end, cost in edges:
            if (result[start] != -2147483647 and result[end] < result[start] - cost + earn_moneys[end]):
                result[end] = result[start] - cost + earn_moneys[end]

                if (count == n-1):
                    is_has_plus_cycle = True
                    cycle_vertices.append(end)
                
    if (result[e] == -2147483647):
        print('gg')
        return
    
    if (is_has_plus_cycle and is_reachable(cycle_vertices, e)):
        print('Gee')
        return
    
    print(result[e])
    
n, s, e, m = map(int, input().split())
edges = []
adj_vertices = defaultdict(list)

for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))
    adj_vertices[start].append(end)

earn_moneys = list(map(int, input().split()))
result = [-2147483647] * (n)
result[s] = earn_moneys[s]

solution()