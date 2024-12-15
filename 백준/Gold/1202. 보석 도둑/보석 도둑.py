import sys
from bisect import bisect_left
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if (x == parent[x]):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

N, K = map(int, input().split())
C = []
jewel_list = []
parent = [i for i in range(K+1)]

for _ in range(N):
    W, V = map(int, input().split())
    jewel_list.append((W, V))

for _ in range(K):
    C.append(int(input()))

C.sort()
jewel_list.sort(key= lambda x: (-x[1], x[0]))
answer = 0

for jewel_w, jewel_v in jewel_list:
    idx = bisect_left(C, jewel_w)
    available_idx = find(idx)

    if (available_idx >= K):
        continue

    answer += jewel_v
    parent[available_idx] += 1

print(answer)
