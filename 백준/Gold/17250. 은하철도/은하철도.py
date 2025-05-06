import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if x < y:
        parent[y] = x
        galaxy_size_dict[x] += galaxy_size_dict[y]
    else:
        parent[x] = y
        galaxy_size_dict[y] += galaxy_size_dict[x]

N, M = map(int, input().split())
parent = [i for i in range(N)]
galaxy_size_dict = dict()

for i in range(N):
    galaxy_size_dict[i] = int(input())

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    
    union(u, v)
    print(galaxy_size_dict[find(u)])