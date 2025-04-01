import sys
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
        return
    
    if (x < y):
        group_id_set.discard(y)
        group_id_set.add(x)
        parent[y] = x
    else:
        group_id_set.discard(x)
        group_id_set.add(y)
        parent[x] = y

N = int(input())
parent = [i for i in range(N+1)]
group_id_set = set(range(1, N+1))

for _ in range(N-2):
    u, v = map(int, input().split())

    union(u, v)

print(*group_id_set)