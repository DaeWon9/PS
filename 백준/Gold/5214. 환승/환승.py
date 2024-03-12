import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, K, M = map(int, input().split())
hyper_tube_dict = defaultdict(tuple)
adj_hyper_tubes = defaultdict(list)
visited = [False for _ in range(N + 1)]

for tube_id in range(M):
    hyper_tube_info = tuple(map(int, input().split()))
    hyper_tube_dict[tube_id] = hyper_tube_info

    for v in hyper_tube_info:
        adj_hyper_tubes[v].append(tube_id)

queue = deque()
queue.append((1, 1)) #time, vertex
visited[1] = True

while queue:
    time, vertex = queue.popleft()

    if (vertex == N):
        print(time)
        exit(0)
    
    for hyper_tube in adj_hyper_tubes[vertex]:
        for adj_vertex in hyper_tube_dict[hyper_tube]:
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                queue.append((time + 1, adj_vertex))

print(-1)