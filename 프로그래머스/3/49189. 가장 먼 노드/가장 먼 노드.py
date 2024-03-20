from collections import deque, defaultdict

def solution(n, edge):
    visited = [False for _ in range(n + 1)]
    adj_vertices = defaultdict(list)
    distance = [21427483647 for _ in range(n + 1)]
    distance[1] = 0
    max_distance = 0
    answer = 0
    
    for v1, v2 in edge:
        adj_vertices[v1].append(v2)
        adj_vertices[v2].append(v1)

    queue = deque()
    queue.append((1, 0))
    visited[1] = True
    
    while queue:
        v, d = queue.popleft()
        
        for adj_vertex in adj_vertices[v]:
            if (not visited[adj_vertex]):
                queue.append((adj_vertex, d + 1))
                distance[adj_vertex] = d + 1
                visited[adj_vertex] = True
    
    max_distance = max(distance[1:])
    answer = distance.count(max_distance)
    
    return answer