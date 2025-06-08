import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):
    if (x == parent[x]):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return False
    
    if (x < y):
        parent[y] = x
    else:
        parent[x] = y
    return True

def dfs(u, p):
    for v, w in mst_adj[u]:
        if (v != p):
            depth[v] = depth[u] + 1
            up[0][v] = u
            max_edge[0][v] = w
            dfs(v, u)

def get_max(u, v):
    if (depth[u] < depth[v]):
        u, v = v, u
    res = 0
    # u를 v와 같은 깊이로
    for k in range(LOG-1, -1, -1):
        if (depth[u] - (1 << k) >= depth[v]):
            res = max(res, max_edge[k][u])
            u = up[k][u]

    if (u == v):
        return res
    
    for k in range(LOG-1, -1, -1):
        if (up[k][u] != -1 and up[k][u] != up[k][v]):
            res = max(res, max_edge[k][u], max_edge[k][v])
            u = up[k][u]
            v = up[k][v]

    res = max(res, max_edge[0][u], max_edge[0][v])
    return res
            

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

default_w = 0
mst_edges = set()
mst_adj = [[] for _ in range(N + 1)]

sorted_edges = sorted(edges)

for w, u, v in sorted_edges:
    if union(u, v):
        # print(u, v, "is mst edge weight: ", w)
        mst_edges.add((min(u, v), max(u, v), w))
        default_w += w
        mst_adj[u].append((v, w))
        mst_adj[v].append((u, w))

LOG = 18
up = [[-1] * (N + 1) for _ in range(LOG)]
max_edge = [[0] * (N + 1) for _ in range(LOG)]
depth = [0] * (N + 1)

dfs(1, -1)

for k in range(1, LOG):
    for v in range(1, N + 1):
        if up[k-1][v] != -1:
            up[k][v] = up[k-1][up[k-1][v]]
            max_edge[k][v] = max(max_edge[k-1][v], max_edge[k-1][up[k-1][v]])

for w, u, v in edges:
    if (min(u, v), max(u, v), w) in mst_edges:
        print(default_w)
    else:
        max_w = get_max(u, v)
        print(default_w + w - max_w)
