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
        group.discard(y)
        group.add(x)
        parent[y] = x
    else:
        group.discard(x)
        group.add(y)
        parent[x] = y

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
adj_vertices = [set() for _ in range(N+1)]
targets = []
answer = ['']

group = set()
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj_vertices[u].add(v)
    adj_vertices[v].add(u)

for _ in range(N):
    targets.append(int(input()))

for i in range(N-1, -1, -1):
    rv = targets[i]
    visited[rv] = True

    if (not group):
        group.add(rv)
        answer.append('YES')
        continue

    union_flag = False

    for vv in adj_vertices[rv]:
        if (visited[vv]):
            union(rv, vv)
            union_flag = True

    if (not union_flag):
        group.add(rv)

    if (len(group) == 1):
        answer.append('YES')
    else:
        answer.append('NO')

for ans in reversed(answer):
    print(ans)