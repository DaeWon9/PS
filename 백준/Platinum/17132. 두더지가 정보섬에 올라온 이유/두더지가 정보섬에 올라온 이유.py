import sys
input = sys.stdin.readline

def find(x):
    if (x == parent[x]):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y, w):
    global answer
    x = find(x)
    y = find(y)

    if (x == y):
        return
    
    answer += w * size[x] * size[y]

    if (x < y):
        parent[y] = x
        size[x] += size[y]
    else:
        parent[x] = y
        size[y] += size[x]

N = int(input())

parent = [i for i in range(N+1)]
size = [1 for _ in  range(N+1)]
edges = []
answer = 0

for _ in range(N-1):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort(reverse=True)

for w, u, v in edges:
    union(u, v, w)

print(answer)