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
        return False
    if (x < y):
        parent[y] = x
    else:
        parent[x] = y
    return True

n, m, k = map(int, input().split())
blue_edges = []
red_edges = []

for _ in range(m):
    c, u, v = map(str, input().rstrip().split())
    u = int(u)
    v = int(v)
    if (c == 'B'):
        blue_edges.append((u, v))
    else:
        red_edges.append((u, v))

parent = [i for i in range(n+1)]
edges_used = 0
min_blue_edges = set()

for u, v in red_edges:
    if (union(u, v)):
        edges_used += 1

for u, v in blue_edges:
    if (edges_used == n-1):
        break
    if (union(u, v)):
        min_blue_edges.add((u, v))
        edges_used += 1

parent = [i for i in range(n+1)]
result = []
blue_count = 0
edges_used = 0

for u, v in min_blue_edges:
    if (union(u, v)):
        result.append((u, v))
        blue_count += 1
        edges_used += 1

for u, v in blue_edges:
    if (blue_count == k):
        break
    if ((u, v) in min_blue_edges):
        continue
    if (union(u, v)):
        result.append((u, v))
        blue_count += 1
        edges_used += 1

for u, v in red_edges:
    if (edges_used == n-1):
        break
    if (union(u, v)):
        result.append((u, v))
        edges_used += 1

if (edges_used == n-1 and blue_count == k):
    for u, v in result:
        print(u, v)
else:
    print(0)