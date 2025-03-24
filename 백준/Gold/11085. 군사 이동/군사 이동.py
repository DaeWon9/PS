import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def find(x):
    if (x == parent[x]):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y, w):
    x = find(x)
    y = find(y)

    if (x == y):
        min_width_dict[x] = min(min_width_dict[x], w)
        return
    
    if (x < y):
        min_width_dict[x] = min(min_width_dict[x], min_width_dict[y], w)
        parent[y] = x
    else:
        min_width_dict[y] = min(min_width_dict[x], min_width_dict[y], w)
        parent[x] = y

p, w = map(int, input().split())
c, v = map(int, input().split())
if (c > v):
    c, v = v, c

min_width_dict = defaultdict(lambda: 1000)

heap = []
parent = [i for i in range(p)]

for _ in range(w):
    s, e, w = map(int, input().split())
    heapq.heappush(heap, (-w, s, e))

while heap:
    w, s, e = heapq.heappop(heap)
    w = -w

    union(s, e, w)

    if (find(c) == find(v)):
        break

print(min_width_dict[find(c)])