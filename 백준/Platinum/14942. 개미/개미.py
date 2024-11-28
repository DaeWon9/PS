import sys
from collections import defaultdict
input = sys.stdin.readline

D = 18
N = int(input())

ants = [int(input()) for _ in range(N)]
edge_dict = defaultdict(list)

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    edge_dict[a-1].append((b-1, c))
    edge_dict[b-1].append((a-1, c))

parents = [[(0, 0) for _ in range(D)] for _ in range(N)]
result = [0 for _ in range(N)]

visited = [False for _ in range(N)]
visited[0] = True

def dfs(node):
    for nxt, cost in edge_dict[node]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        parents[nxt][0] = (node, cost)
        dfs(nxt)

def parent_init() :
    for d in range(1, D) :
        for node in range(N) :
            pnode, pcost = parents[node][d-1]
            gpnode, gpcost = parents[pnode][d-1]
            parents[node][d] = (gpnode, pcost+gpcost)

def search(idx, cur, left) :
    if cur == 0:
        result[idx] = cur + 1
        return
    
    for d in range(D-1, -1, -1) :
        pnode, pcost = parents[cur][d]
        if left >= pcost :
            search(idx, pnode, left-pcost)
            return
    result[idx] = cur + 1

dfs(0)
parent_init()
for i in range(N) :
    search(i, i, ants[i])
print(*result, sep = '\n')