import sys
input = sys.stdin.readline

def find(x, parent):
    if (x != parent[x]):
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, size):
    x = find(x, parent)
    y = find(y, parent)

    if (x == y):
        return False 

    if (x < y):
        parent[y] = x
        size[x] += size[y]
    else:
        parent[x] = y
        size[y] += size[x]
    return True

while True:
    n, m, k = map(int, input().split())

    if (n == 0 and m == 0 and k == 0):
        break

    blue_edges = []
    red_edges = []

    for _ in range(m):
        c, u, v = input().split()
        u, v = int(u), int(v)
        if (c == 'B'):
            blue_edges.append((u, v))
        else:
            red_edges.append((u, v))

    parent = [i for i in range(n+1)]
    size = [1 for _ in range(n+1)]
    max_blue = 0
    edge_count = 0

    for u, v in blue_edges:
        if (union(u, v, parent, size)):
            max_blue += 1
            edge_count += 1

    for u, v in red_edges:
        if (edge_count == n - 1):
            break
        if (union(u, v, parent, size)):
            edge_count += 1

    parent = [i for i in range(n+1)]
    size = [1 for _ in range(n+1)]
    min_blue = 0
    edge_count = 0

    for u, v in red_edges:
        if (union(u, v, parent, size)):
            edge_count += 1

    for u, v in blue_edges:
        if (edge_count == n - 1):
            break
        if (union(u, v, parent, size)):
            min_blue += 1
            edge_count += 1

    print(1 if min_blue <= k <= max_blue else 0)
