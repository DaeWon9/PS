import sys
input = sys.stdin.readline

# A - B - C - D - E
# 주위 사람의 수 N(1 ≤ N ≤ 2,000)
# 적대관계의 수 M(0 ≤ M ≤ 1,000,000)

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
    
    if (x < y):
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
enemy = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    a = find(A)
    b = find(B)
    
    if (a == b):
        print(0)
        exit(0)

    if (enemy[a]):
        union(enemy[a], b)
    else:
        enemy[a] = b
    if (enemy[b]):
        union(enemy[b], a)
    else:
        enemy[b] = a

print(1)