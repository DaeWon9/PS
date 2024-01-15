import sys
from collections import deque, defaultdict

city_count = int(sys.stdin.readline())
bus_count = int(sys.stdin.readline())

graph = []
costs = [[2147483647 for _ in range(city_count + 1)] for _ in range(city_count + 1)]
min_cost_graph = [2147483647 for _ in range(city_count + 1)]
connected_city = defaultdict(list)

for _ in range(bus_count):
    start, end, cost = map(int, sys.stdin.readline().split())
    if (cost >= costs[start][end]):
        continue
    connected_city[start].append(end)
    costs[start][end] = cost


ori, des = map(int, sys.stdin.readline().split())
min_cost_graph[ori] = 0

queue = deque()

for city in connected_city[ori]:
    queue.append([ori, city]) 

while queue:
    temp_ori, temp_des = queue.popleft()

    temp_des_cost = min_cost_graph[temp_ori] + costs[temp_ori][temp_des]
    if (temp_des_cost < min_cost_graph[temp_des]):
        min_cost_graph[temp_des] = temp_des_cost

        for city in connected_city[temp_des]:
            queue.append([temp_des, city]) 

print(min_cost_graph[des])