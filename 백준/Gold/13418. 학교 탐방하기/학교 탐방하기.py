import sys
input = sys.stdin.readline

def find(x):
    if (parent[x] == x):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if (x == y):
        return
    
    if (x < y):
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
edges = []
default_fatigue = 0

v1, v2, case = map(int, input().split())
if (case == 0): # 오르막길
    default_fatigue = 1
else:
    default_fatigue = 0

for _ in range(M):
    v1, v2, case = map(int, input().split())
    edges.append((v1, v2, not case)) # 오르막이 0 임


max_fatigue = default_fatigue
min_fatigue = default_fatigue

parent = [i for i in range(N + 1)]
edges.sort(key = lambda x : x[2])

for v1, v2, cost in edges:
    if (find(v1) != find(v2)):
        min_fatigue += cost
        union(v1, v2)

parent = [i for i in range(N + 1)]
edges.sort(key = lambda x : -x[2])

for v1, v2, cost in edges:
    if (find(v1) != find(v2)):
        max_fatigue += cost
        union(v1, v2)

print((max_fatigue - min_fatigue) * (max_fatigue + min_fatigue))