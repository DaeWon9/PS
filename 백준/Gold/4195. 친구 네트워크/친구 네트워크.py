import sys
from collections import defaultdict
input = sys.stdin.readline

def find(x):
    if (x == parent[x]):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return group_count_dict[x]
    
    if (x < y):
        group_count_dict[x] += group_count_dict[y]
        parent[y] = x
        return group_count_dict[x]
    else:
        group_count_dict[y] += group_count_dict[x]
        parent[x] = y
        return group_count_dict[y]

T = int(input())

for t in range(T):
    F = int(input())
    parent = [i for i in range(200001)]
    id_dict = defaultdict(int)
    group_count_dict = defaultdict(lambda: 1)
    id = 1

    for _ in range(F):
        u, v = map(str, input().rstrip().split())

        if (u not in id_dict):
            id_dict[u] = id
            id += 1

        if (v not in id_dict):
            id_dict[v] = id
            id += 1

        print(union(id_dict[u], id_dict[v]))