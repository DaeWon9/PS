import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    INF = 10_000_001
    answer = [50_001, INF]
    summits = set(summits)
    gates = set(gates)
    adj_vertices = defaultdict(list)
    heap = []
    dp = [INF] * (n+1)
    
    for u, v, d in paths:
        adj_vertices[u].append((v, d))
        adj_vertices[v].append((u, d))

    for gate in gates: # 출발지점
        dp[gate] = 0
        heapq.heappush(heap, (0, gate))
        
        while heap:
            intensity, cur = heapq.heappop(heap)
            
            if (dp[cur] < intensity):
                continue

            if (cur in summits): # 더이상 뻗어나가지 못하게 continue
                if (answer[1] > intensity):
                    answer = [cur, intensity]
                elif (answer[1] == intensity):
                    answer = [min(answer[0], cur), intensity]
                continue

            for adj_vertex, dist in adj_vertices[cur]:                
                if (adj_vertex in gates): # 다른 시작지점은 방문 불가능
                    continue
                
                new_intensity = max(intensity, dist)
                
                if (dp[adj_vertex] > new_intensity):
                    dp[adj_vertex] = new_intensity
                    heapq.heappush(heap, (new_intensity, adj_vertex))
                    
    return answer