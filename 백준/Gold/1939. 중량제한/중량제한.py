import sys
from collections import deque, defaultdict
import heapq
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

# 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
heap = []
adj_vertices = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(heap, (-C, A, B))

g1, g2 = map(int, input().split())

while heap:
    c, a, b = heapq.heappop(heap)
    c = -c

    if (find(a) == find(b)):
        continue
    
    union(a, b)
    adj_vertices[a].append((b, c))
    adj_vertices[b].append((a, c))

answer = 0
queue = deque()
visited = set()
queue.append((g1, 1000000000))

while queue:
    v, min_weight = queue.popleft()

    if (v == g2):
        answer = max(answer, min_weight)
        continue

    for adj_vertex, weight in adj_vertices[v]:
        if ((v, adj_vertex) in visited):
            continue

        visited.add((v, adj_vertex))
        queue.append((adj_vertex, min(min_weight, weight)))

print(answer)