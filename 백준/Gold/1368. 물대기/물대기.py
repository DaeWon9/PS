import sys
import heapq
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
    
    if (rank[x] < rank[y]): #x의 rank가 낮음
        parent[x] = y
        rank[y] += rank[x]
    elif (rank[y] < rank[x]):
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]

N = int(input())
parent = [i for i in range(N + 1)]
rank = [1 for _ in range(N + 1)]
min_cost = 0
edges = []

for i in range(N):
    heapq.heappush(edges, (int(input()), 0, i + 1))

for r in range(N):
    input_data = list(map(int, input().split()))
    for c in range(r + 1, N):
        heapq.heappush(edges, (input_data[c], r + 1, c + 1))

while edges:
    cost, r, c = heapq.heappop(edges)

    if (find(r) != find(c)):
        union(r, c)
        min_cost += cost

print(min_cost)