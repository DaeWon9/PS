import sys
from collections import defaultdict
input = sys.stdin.readline

# 술마다 고유 ID 지정
# 술병을 저장할 수 있는 두개의 공간이 추가되면, 이미 추가된 공간과 공유
# 공유되는 공간을 하나의 집합으로 관리 - DSU

def find(x):
    if (parent[x] == x):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return x
    
    if (x < y):
        parent[y] = x
        group_remain_space[x] += group_remain_space[y]
        for v in linked_space[y]:
            parent[v] = x
        return x
    else:
        parent[x] = y
        group_remain_space[y] += group_remain_space[x]
        for v in linked_space[x]:
            parent[v] = y
        return y

N, L = map(int, input().split())
parent = [i for i in range(L + 1)]
visit = [False for _ in range(L + 1)]
group_remain_space = [0 for _ in range(L + 1)]
linked_space = defaultdict(list)

for id in range(1, N + 1):
    a, b = map(int, input().split())
    linked_space[a].append(b)
    linked_space[b].append(a)

    root = union(a, b)

    if (not visit[a]):
        group_remain_space[root] += 1
        visit[a] = True
    
    if (not visit[b]):
        group_remain_space[root] += 1
        visit[b] = True

    if (group_remain_space[root] > 0):
        group_remain_space[root] -= 1
        print("LADICA")
    else:
        print("SMECE")