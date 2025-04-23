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
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
adj_vertices = [[] for _ in range(N+1)]
targets = []
answer = ['DISCONNECT']

visited = [False] * (N+1)
groups = set()

for _ in range(M):
    u, v = map(int, input().split())
    adj_vertices[u].append(v)
    adj_vertices[v].append(u)

for _ in range(N):
    targets.append(int(input()))

for i in range(N-1, -1, -1):
    rv = targets[i]
    visited[rv] = True
    
    if (not groups):
        groups.add(rv)
        answer.append('CONNECT')
        continue

    connected = False
    for vv in adj_vertices[rv]:
        if visited[vv]:
            if (find(rv) != find(vv)):
                groups.discard(find(rv))
                groups.discard(find(vv))
                union(rv, vv)
                groups.add(find(rv))
            connected = True

    if (not connected):
        groups.add(rv)

    if (len(groups) == 1):
        answer.append('CONNECT')
    else:
        answer.append('DISCONNECT')

for ans in reversed(answer):
    print(ans)
