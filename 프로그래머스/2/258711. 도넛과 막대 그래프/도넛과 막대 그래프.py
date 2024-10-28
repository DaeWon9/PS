# 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.
# 생성한 정점은 진입차수 0, 진출차수가 2이상인 정점이다.
# 생성한 정점을 제외하면 각각의 그래프는 독립적으로 존재한다.

# 도넛은 출발 후 자기 자신에게 도착
# 막대는 출발 후 돌아오지 않고 종료
# 8자는 진출차수 2, 진입차수 2인 정점의 개수

from collections import defaultdict, deque

def find_graph_type(start):
    start_count = 0
    q = deque([start])
    visited = set()
    
    while q:
        v = q.popleft()
        
        if (v == start):
            start_count += 1
            
        if (start_count > 1):
            break
        
        for adj_vertex in adj_vertices[v]:
            if (adj_vertex not in visited):
                visited.add(adj_vertex)
                q.append(adj_vertex)
                
    if (start_count == 2):
        for vertex in visited:
            if (in_degree[vertex] == 2 and out_degree[vertex] == 2):
                return 3 # 8자 
        
        return 1 # 도넛
    else:
        return 2 # 막대

in_degree = defaultdict(lambda: 0)
out_degree = defaultdict(lambda: 0)
adj_vertices = defaultdict(list)
    
def solution(edges):
    init_vertex = 0    
    answer = [0, 0, 0, 0] # 도넛, 막대, 8자
    
    for v1, v2 in edges: # v1 -> v2
        in_degree[v2] += 1
        out_degree[v1] += 1
        adj_vertices[v1].append(v2)
        
    for vertex in out_degree:
        if (in_degree[vertex] == 0 and out_degree[vertex] > 1):
            init_vertex = vertex
    
    answer[0] = init_vertex
    queue = deque()
    for adj_vertex in adj_vertices[init_vertex]:
        queue.append(adj_vertex)
        in_degree[adj_vertex] -= 1
        
    for vertex in out_degree:        
        if (in_degree[vertex] == 2 and out_degree[vertex] == 2):
            answer[3] += 1
    
    while queue:
        start_vertex = queue.popleft()
        
        graph_type = find_graph_type(start_vertex)
        
        if (graph_type != 3):
            answer[graph_type] += 1
        
    return answer