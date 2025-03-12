import sys
from collections import defaultdict
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

N, M, k = map(int, input().split())
A = list(map(int, input().split()))
group_cost = defaultdict(lambda: 10001)
answer = 0
parent = [i for i in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split()) # u, v 는 친구
    union(u, v)

for i in range(1, N+1):
    group = find(parent[i])
    friend_cost = A[i-1]
    group_cost[group] = min(group_cost[group], friend_cost)

for group in group_cost.keys():
    answer += group_cost[group]

if (answer <= k):
    print(answer)
else:
    print('Oh no')