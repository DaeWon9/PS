import sys
input = sys.stdin.readline

# 결국 연결되어있는 여행지면 가능.
# union - find로 분리집합

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

    if (rank[x] < rank[y]):
        parent[x] = y
    elif (rank[y] < rank[x]):
        parent[y] = x
    else:
        rank[y] += 1
        parent[x] = y

N = int(input())
M = int(input())
parent = [i for i in range(N)]
rank = [0 for _ in range(N)]

if (M == 1):
    print('YES')
    exit(0)
    
for r in range(N):
    input_data = list(map(int, input().split()))
    for c in range(N):
        if (input_data[c] == 1):
            if (find(r) != find(c)):
                union(r, c)

schedule = list(map(int, input().split()))
group_id = find(schedule[0] - 1)

for city in schedule[1:]:
    temp = find(city - 1)
    if (group_id != temp):
        print('NO')
        exit(0)

print('YES')