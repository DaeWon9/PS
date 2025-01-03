import sys
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

N, M = map(int, input().split())
school_info = [''] + list(map(str, input().rstrip().split()))
parent = [i for i in range(N+1)]
heap = []
answer = 0

for _ in range(M):
    u, v, d = map(int, input().split())

    if (school_info[u] == school_info[v]):
        continue

    heapq.heappush(heap, (d, u, v))

while heap:
    d, u, v = heapq.heappop(heap)

    if (find(u) == find(v)):
        continue

    union(u, v)
    answer += d

root_set = set(find(i) for i in range(1, N+1))
if (len(root_set) == 1):
    print(answer)
else:
    print(-1)