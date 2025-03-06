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

def get_distance(ch):    
    if (ch == '0'):
        return 0
    if ('a' <= ch <= 'z'):
        return (ord(ch) - 96)
    if ('A' <= ch <= 'Z'):
        return (ord(ch) - 38)

N = int(input())
heap = []
parent = [i for i in range(N)]
answer = 0

for i in range(N):
    input_data = input().rstrip()
    for j in range(N):
        dist = get_distance(input_data[j])
        answer += dist

        if (i == j):
            continue

        if (dist == 0):
            continue

        heapq.heappush(heap, (dist, i, j))

while heap:
    d, u, v = heapq.heappop(heap)

    if (find(u) == find(v)):
        continue

    answer -= d
    union(u, v)

if (len(set(find(i) for i in range(N))) != 1):
    print(-1)
else:
    print(answer)