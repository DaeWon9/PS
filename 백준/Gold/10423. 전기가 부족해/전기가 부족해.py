import sys
import heapq
input = sys.stdin.readline

def find(x):
    if (parent[x] == x):
        return x
    
    compression_parent = find(parent[x])
    parent[x] = compression_parent

    if (compression_parent in K_list):
        status_list[x] = True

    return compression_parent

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return
    
    if (x in K_list):
        status_list[y] = True
        parent[y] = x
        return
    
    if(y in K_list):
        status_list[x] = True
        parent[x] = y
        return
    
    if (x < y): # 작은게 부모로
        parent[y] = x
    else:
        parent[x] = y

N, M, K = map(int, input().split())
parent = [i for i in range(N + 1)]
K_list = set(map(int, input().split()))
status_list = [False for _ in range(N + 1)]
status_list[0] = True

for K in K_list:
    status_list[K] = True

edges = []
answer = 0

for _ in range(M):
    v1, v2, cost = map(int, input().split())
    heapq.heappush(edges, (cost, v1, v2))

while edges:
    cost, v1, v2 = heapq.heappop(edges)

    if (find(v1) in K_list and find(v2) in K_list):
        continue

    if (find(v1) != find(v2)):
        union(v1, v2)
        answer += cost
    
    if (False not in status_list):
        break
    
print(answer)