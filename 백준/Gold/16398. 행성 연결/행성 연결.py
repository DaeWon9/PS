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
    
    if (rank[x] < rank[y]):
        parent[x] = y
        rank[y] += rank[x]
    elif (rank[y] < rank[x]):
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y 
        rank[y] += rank[x]

N = int(input())
edges = []
parent = [i for i in range(N)]
rank = [0 for _ in range(N)]
answer = 0

for r in range(N):
    input_data = list(map(int, input().split()))    
    
    for c in range(r + 1, N):
        heapq.heappush(edges, (input_data[c], r, c))

while edges:
    cost, v1, v2 = heapq.heappop(edges)

    if (find(v1) != find(v2)):
        answer += cost
        union(v1, v2)

print(answer)