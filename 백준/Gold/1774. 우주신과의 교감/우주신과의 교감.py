import sys
import heapq
import math
input = sys.stdin.readline

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
    
    if (x < y): # 작은게 부모
        parent[y] = x
    else:
        parent[x] = y

def get_distance(pos1, pos2):
    x_diff = pos1[0] - pos2[0]
    y_diff = pos1[1] - pos2[1]
    return math.sqrt(x_diff ** 2 + y_diff ** 2)

N, M = map(int, input().split())
pos_info_list = [[0, 0]]
already_connected_list = []
heap = []

parent = [i for i in range(N + 1)]

for _ in range(N):
    pos_info_list.append(tuple(map(int, input().split())))

for _ in range(M):
    already_connected_list.append(tuple(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        distance = get_distance(pos_info_list[i], pos_info_list[j])
        heapq.heappush(heap, (distance, i, j))

answer = 0
for id1, id2 in already_connected_list:
    if (find(id1) != find(id2)):
        distance = get_distance(pos_info_list[id1], pos_info_list[id2])
        union(id1, id2)

while heap:
    cost, v1, v2 = heapq.heappop(heap)

    if (find(v1) != find(v2)):
        union(v1, v2)

        answer += cost

print("{:.2f}".format(answer))