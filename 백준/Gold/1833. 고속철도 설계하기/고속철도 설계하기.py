import sys
import heapq
from collections import deque
input = sys.stdin.readline

def get_index(row, col):
    return N * row + col

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
    
    if (y < x):
        parent[x] = y
    else:
        parent[y] = x

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

heap = []
default_cost = 0
answer = 0
road_info = []

already_connected_city_queue = deque()
parent = [i for i in range(N * N)]

for row in range(N):
    input_data = list(map(int, input().split()))

    for col in range(row + 1, N):
        cost = input_data[col]
        if (cost < 0):
            default_cost -= cost
            already_connected_city_queue.append((row, col))
        else:
            heapq.heappush(heap, (cost, row, col))
            
while already_connected_city_queue:
    row, col = already_connected_city_queue.popleft()
    
    if (find(row) != find(col)):
        union(row, col)

while heap:
    cost, row, col = heapq.heappop(heap)

    if (find(row) != find(col)):
        union(row, col)
        road_info.append((row, col))
        answer += cost

print(answer + default_cost, len(road_info))
for row, col in road_info:
    print(row + 1, col + 1)