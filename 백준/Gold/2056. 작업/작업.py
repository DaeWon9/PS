import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
time_list = [0 for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
adj_vertices = [[] for _ in range(N + 1)]

queue = deque()
result = [0 for _ in range(N + 1)]

for id in range(1, N + 1):
    input_data = list(map(int, input().split()))
    
    time_list[id] = input_data[0]
    indegree[id] = input_data[1]

    for vertex in input_data[2:]:
        adj_vertices[vertex].append(id)

for id in range(1, N + 1):
    if (indegree[id] == 0):
        queue.append(id)
        result[id] = time_list[id]

while queue:
    v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        result[adj_vertex] = max(result[adj_vertex], result[v] + time_list[adj_vertex])

        if (indegree[adj_vertex] == 0):
            queue.append(adj_vertex)

print(max(result))