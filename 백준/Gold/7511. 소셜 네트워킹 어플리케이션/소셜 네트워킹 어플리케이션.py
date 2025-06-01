import sys
input = sys.stdin.readline

def find(x, parent):
    if (x == parent[x]):
        return x
    
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)

    if (x == y):
        return
    
    if (x < y):
        parent[y] = x
    else:
        parent[x] = y

T = int(input())

for t in range(1, T+1):
    print("Scenario " + str(t) + ":")
    n = int(input()) # 유저의 수 (1 ≤ n ≤ 10^6)
    k = int(input()) # 친구 관계의 수 (1 ≤ k ≤ 10^5)

    parent = [i for i in range(n)]

    for _ in range(k):
        a, b = map(int, input().split()) # a와 b는 친구
        union(a, b, parent)

    m = int(input()) # 미리 구할 쌍의 수 (1 ≤ m ≤ 10^5)
    for _ in range(m):
        u, v = map(int, input().split()) # 구해야하는 쌍
        if (find(u, parent) == find(v, parent)):
            print(1)
        else:
            print(0)
    
    print()