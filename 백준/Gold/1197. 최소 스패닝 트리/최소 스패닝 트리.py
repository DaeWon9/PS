import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if root[x] == x:
        return x
    
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    root[y] = x

V, E = map(int, input().split())

edges = []
for _ in range(E):
    edges.append(list(map(int, input().split())))

root = defaultdict(int)
for i in range(1, V+1):
    root[i] = i

edges = sorted(edges, key=lambda x: x[2])
weight = 0

for edge in edges:
    if find(edge[0]) == find(edge[1]):
        continue

    weight += edge[2]
    union(edge[0], edge[1])

print(weight)