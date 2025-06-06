import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

LOG = 16

def dfs(v, d):
    depth[v] = d
    visited[v] = True

    for adj_vertex in adj_vertices[v]:
        if (not visited[adj_vertex]):
            parent[adj_vertex][0] = v
            dfs(adj_vertex, d + 1)

def lca(u, v):
    if (depth[u] > depth[v]): # u의 depth가 더 작게 유지
        u, v = v, u
    
    for i in range(LOG - 1, -1, -1):
        if (depth[v] - depth[u] >= 1 << i):
            v = parent[v][i]

    if (u == v):
        return u
    
    for i in range(LOG - 1, -1, -1):
        if (parent[u][i] != parent[v][i]):
            u = parent[u][i]
            v = parent[v][i]
        
    return parent[u][0]

N = int(input())
adj_vertices = defaultdict(list)
depth = [0 for _ in range(N+1)]
parent = [[0] * LOG for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())

    adj_vertices[u].append(v)
    adj_vertices[v].append(u)

dfs(1, 0)

for i in range(1, LOG):
    for j in range(1, N+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

M = int(input())

for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
