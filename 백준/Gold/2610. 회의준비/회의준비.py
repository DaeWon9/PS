import sys
input = sys.stdin.readline

# 그룹 나누고
# 각 그룹별 거리 구하고
# 노드간의 거리의 합이 최소가 되는 정점이 정답
# N <= 100 -> 플로이드 100 * 100 * 100 = 1000000

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
        group_vertex_dict[x] += group_vertex_dict[y]
        del group_vertex_dict[y]
        parent[y] = x
    else:
        group_vertex_dict[y] += group_vertex_dict[x]
        del group_vertex_dict[x]
        parent[x] = y

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]
group_vertex_dict = dict()
adj_vertices = [[] for _ in range(N+1)]
distance = [[101 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    group_vertex_dict[i] = [i]
    distance[i][i] = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj_vertices[u].append(v)
    adj_vertices[v].append(u)
    distance[u][v] = 1
    distance[v][u] = 1

    union(u, v)

for i in range(1, N+1):
    find(i)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

print(len(group_vertex_dict))

result = []
for key in group_vertex_dict:
    target_vertices = group_vertex_dict[key]
    answer = 0
    min_dist = 101
    for u in target_vertices:
        temp_dist = 0
        for v in target_vertices:
            if (u == v): continue
            temp_dist = max(temp_dist, distance[u][v])
        
        if (temp_dist < min_dist):
            min_dist = temp_dist
            answer = u
    result.append(answer)

result.sort()
for r in result:
    print(r)
