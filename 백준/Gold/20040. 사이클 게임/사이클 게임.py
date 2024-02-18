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
    else: # rank same
        rank[y] += 1
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]
answer = 0

for time in range(m):
    v1, v2 = map(int, input().split())

    if (find(v1) == find(v2)):
        answer = time + 1
        break

    union(v1, v2)

print(answer)