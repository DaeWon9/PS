import sys
from collections import defaultdict
input = sys.stdin.readline

def find(x):
    if (x == root[x]):
        return x
    
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return
    
    x_candy_count = C[x]
    if (x in group_candy_info):
        x_candy_count = group_candy_info[x][0]
    
    y_candy_count = C[y]
    if (y in group_candy_info):
        y_candy_count = group_candy_info[y][0]
    
    if (x < y):
        root[y] = x
        group_candy_info[x] = [x_candy_count + y_candy_count, group_candy_info[x][1] + group_candy_info[y][1]]
        all_group_set.discard(y)
    else:
        root[x] = y
        group_candy_info[y] = [x_candy_count + y_candy_count, group_candy_info[x][1] + group_candy_info[y][1]]
        all_group_set.discard(x)

N, M, K = map(int, input().split())
C = list(map(int, input().split()))
dp = [0] * K 

root = [i for i in range(N)]
group_candy_info = defaultdict(lambda: [0, 1])
all_group_set = set(range(N))

for i in range(N):
    group_candy_info[i] = [C[i], 1]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    union(a, b)

for group in all_group_set:
    candy_count, group_size = group_candy_info[group]

    for k in range(K-1, group_size-1, -1):
        dp[k] = max(dp[k-group_size] + candy_count, dp[k])

print(max(dp))