import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def find(x, parent):
    if (x == parent[x]):
        return x
    
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)

    if (x == y):
        return
    
    if (x < y):
        parent[y] = x
    else:
        parent[x] = y

def solve(start, parent, used_edges, w, path: list = []):
    global answer, min_w

    if (len(path) == N-1):
        check_set = set(find(i, parent) for i in range(1, N+1))
        if (min_w > w and len(check_set) == 1):
            min_w = w
            answer = path[:]
        return
    
    if (min_w <= w):
        return
    
    for i in range(start, M): # i번째 edge
        ww, uu, vv = edges[i]

        if (used_edges[uu] < B[uu] and used_edges[vv] < B[vv] and (find(uu, parent) != find(vv, parent))):
            prev_parent = parent[:]
            union(uu, vv, parent)
            path.append((uu, vv))
            used_edges[uu] += 1
            used_edges[vv] += 1

            solve(i+1, parent, used_edges, w + ww, path)

            path.pop()
            parent = prev_parent[:]
            used_edges[uu] -= 1
            used_edges[vv] -= 1
        
N, M = map(int, input().split())
B = [0] + list(map(int, input().split()))
edges = []
min_w = float('inf')
answer = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

if (N == 1):
    print('YES')
    exit(0)

edges.sort()
solve(0, [i for i in range(N+1)], [0 for _ in range(N+1)], 0)

if (answer):
    print('YES')

    for edge in answer:
        print(*sorted(edge))
else:
    print('NO')