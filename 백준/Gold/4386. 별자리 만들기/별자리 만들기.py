import sys
import heapq
import math
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

def get_cost(id1, id2):
    star1_x, star1_y = star_dict[id1]
    star2_x, star2_y = star_dict[id2]

    x_diff = star2_x - star1_x
    y_diff = star2_y - star1_y
    cost = math.sqrt((x_diff * x_diff) + (y_diff * y_diff))

    return cost

n = int(input())
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]
edges = []

star_dict = defaultdict(list)
answer = 0

for id in range(n):
    x, y = map(float, input().split())
    star_dict[id] = [x, y]

for i in range(n - 1):
    for j in range(i + 1, n):
        heapq.heappush(edges, (get_cost(i, j), i, j))

while edges:
    cost, star1_id, star2_id = heapq.heappop(edges)

    if (find(star1_id) == find(star2_id)):
        continue

    answer += cost

    union(star1_id, star2_id)

print(round(answer,2))