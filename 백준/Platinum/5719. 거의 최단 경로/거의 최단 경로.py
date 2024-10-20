import sys
import heapq
from collections import defaultdict, deque
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    
    if (N == 0 and M == 0):
        break

    S, D = map(int, input().split())

    adj_vertices = defaultdict(list)
    reversed_adj_vertices = defaultdict(list)

    for _ in range(M):
        v1, v2, t = map(int, input().split())
        
        adj_vertices[v1].append((v2, t))
        reversed_adj_vertices[v2].append((v1, t))
    
    time = [2147483647 for _ in range(N)]
    time[S] = 0
    heap = [(0, S)]

    while heap:
        cur_t, v = heapq.heappop(heap)

        if (time[v] < cur_t):
            continue

        for adj_vertex, t in adj_vertices[v]:
            updated_time = time[v] + t          
            if (time[adj_vertex] > updated_time):
                time[adj_vertex] = updated_time
                heapq.heappush(heap, (updated_time, adj_vertex))

    queue = deque([D])
    visited = [False for _ in range(N)]
    removed_path = set()

    while queue:
        v = queue.popleft()

        for adj_vertex, t in reversed_adj_vertices[v]:
            target_time = time[v] - time[adj_vertex]

            if (target_time == t):
                removed_path.add((adj_vertex, v))

                if (not visited[adj_vertex]):
                    visited[adj_vertex] = True
                    queue.append(adj_vertex)

    answer_time = [2147483647 for _ in range(N)]
    answer_time[S] = 0
    heap = [(0, S)]

    while heap:
        cur_t, v = heapq.heappop(heap)

        if (answer_time[v] < cur_t):
            continue

        for adj_vertex, t in adj_vertices[v]:
            if ((v, adj_vertex) in removed_path):
                continue

            updated_time = answer_time[v] + t          
            if (answer_time[adj_vertex] > updated_time):
                answer_time[adj_vertex] = updated_time
                heapq.heappush(heap, (updated_time, adj_vertex))

    if (answer_time[D] == 2147483647):
        print(-1)
    else:
        print(answer_time[D])