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
    
    if (rank[x] < rank[y]):
        parent[x] = y
    elif (rank[y] < rank[x]):
        parent[y] = x
    else:
        rank[y] += 1
        parent[x] = y

N, M = map(int, input().split())

edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

edges.sort(key = lambda x : x[2])

parent = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]
answer = 0
union_count = 0

for edge in edges:
    v1, v2, w = edge

    if (union_count == N - 2):
        break

    if (find(v1) == find(v2)):
        continue
    
    answer += w
    union(v1, v2)
    union_count += 1

print(answer)