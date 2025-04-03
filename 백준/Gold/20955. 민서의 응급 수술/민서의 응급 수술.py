import sys
input = sys.stdin.readline

# 뉴런을 연결하거나 끊기 가능
# 뉴런을 트리 형태로 연결하기 위한 최소 연산 횟수 

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
        group_id_set.remove(y)
        parent[y] = x
    else:
        group_id_set.remove(x)
        parent[x] = y

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
group_id_set = set(range(1, N+1))

answer = 0

for _ in range(M):
    u, v = map(int, input().split())

    if (find(u) == find(v)): # 이미 연결이 되어있다면 연결 끊기
        answer += 1
    else:
        union(u, v)

answer += len(group_id_set) - 1
print(answer)