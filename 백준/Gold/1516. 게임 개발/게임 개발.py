import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())
building_time_dict = defaultdict(int)
adj_vertices = defaultdict(list)
indegree = [0 for _ in range(N)]
time_list = [0 for _ in range(N)]
queue = deque()

for id in range(N):
    input_data = list(map(int, input().split()))
    building_time_dict[id] = input_data[0]

    for vertex in input_data[1:]:
        if (vertex == -1):
            break
        
        adj_vertices[vertex - 1].append(id)
        indegree[id] += 1

for id in range(N):
    if (indegree[id] == 0):
        queue.append(id)
        time_list[id] = building_time_dict[id]

while queue:
    vertex = queue.popleft()

    for adj_vertex in adj_vertices[vertex]:
        indegree[adj_vertex] -= 1
        time_list[adj_vertex] = max(time_list[adj_vertex], time_list[vertex] + building_time_dict[adj_vertex])

        if (indegree[adj_vertex] == 0):
            queue.append(adj_vertex)
    
for time in time_list:
    print(time)