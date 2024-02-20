import sys
import heapq
from collections import defaultdict
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
    
    if (rank[x] < rank[y]):
        parent[x] = y
    elif (rank[y] < rank[x]):
        parent[y] = x
    else:
        rank[y] += 1
        parent[x] = y

def get_cost(planet_1, planet_2):
    x1, y1, z1 = planet_dict[planet_1]
    x2, y2, z2 = planet_dict[planet_2]

    return min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))

N = int(input())
parent = [i for i in range(N)]
rank = [0 for _ in range(N)]

planet_x_list = []
planet_y_list = []
planet_z_list = []
planet_dict = defaultdict(list)

edges = []
answer = 0

for id in range(N):
    x, y, z = map(int, input().split())
    planet_x_list.append((id, x))
    planet_y_list.append((id, y))
    planet_z_list.append((id, z))
    planet_dict[id] = (x, y, z)

planet_x_list.sort(key = lambda x : x[1])
planet_y_list.sort(key = lambda x : x[1])
planet_z_list.sort(key = lambda x : x[1])

# X 순으로 정렬하면 인접한 행성끼리의 거리 중 X에 한해서는 최소 길이임 -> 후보
for index in range(N - 1):
    planet1_id = planet_x_list[index][0]
    planet2_id = planet_x_list[index + 1][0]
    heapq.heappush(edges, (get_cost(planet1_id, planet2_id), planet1_id, planet2_id))

for index in range(N - 1):
    planet1_id = planet_y_list[index][0]
    planet2_id = planet_y_list[index + 1][0]
    heapq.heappush(edges, (get_cost(planet1_id, planet2_id), planet1_id, planet2_id))

for index in range(N - 1):
    planet1_id = planet_z_list[index][0]
    planet2_id = planet_z_list[index + 1][0]
    heapq.heappush(edges, (get_cost(planet1_id, planet2_id), planet1_id, planet2_id))

while edges:
    cost, v1, v2 = heapq.heappop(edges)

    if (find(v1) == find(v2)):
        continue

    answer += cost
    union(v1, v2)

print(answer)