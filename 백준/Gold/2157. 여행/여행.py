import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M, K = map(int, input().split())
adj_vertices = defaultdict(set)
cost = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for _ in range(K):
    u, v, c = map(int, input().split()) # u -> v 
    if (u > v):
        continue

    adj_vertices[u].add(v)
    cost[u][v] = max(cost[u][v], c)

queue = deque()
queue.append((1, 1, 0))

while queue:
    m, v, c = queue.popleft()

    if (m+1 > M):
        continue

    if (dp[v][m] > c):
        continue

    for adj_vertex in adj_vertices[v]:
        new_cost = c + cost[v][adj_vertex]

        if (dp[adj_vertex][m+1] <= new_cost):
            dp[adj_vertex][m+1] = new_cost
            queue.append((m+1, adj_vertex, new_cost))

print(max(dp[N]))