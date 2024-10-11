import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj_vertices = [[] for _ in range(N + 1)]
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
distance = [2147483647 for _ in range(N + 1)]
min_path = []
answer = 0

for _ in range(M):
    v1, v2, time = map(int, input().split())
    graph[v1][v2] = time
    graph[v2][v1] = time

    adj_vertices[v1].append(v2)
    adj_vertices[v2].append(v1)

queue = deque()
queue.append(([1], 0, 1)) # path, time, vertex

while queue:
    path, time, vertex = queue.popleft()

    if (distance[vertex] < time):
        continue

    for adj_vertex in adj_vertices[vertex]:
        updated_time = time + graph[vertex][adj_vertex]

        if (distance[adj_vertex] > updated_time):
            distance[adj_vertex] = updated_time
            updated_path = path + [adj_vertex]
            queue.append((updated_path, updated_time, adj_vertex))

            if (adj_vertex == N):
                min_path = updated_path

for i in range(len(min_path) - 1):
    path_set = set([(min_path[i], min_path[i + 1]), (min_path[i + 1], min_path[i])])
    distance = [2147483647 for _ in range(N + 1)]
    queue = deque()
    queue.append((0, 1)) # time, vertex

    while queue:
        time, vertex = queue.popleft()

        if (distance[vertex] < time):
            continue

        for adj_vertex in adj_vertices[vertex]:
            if ((vertex, adj_vertex) in path_set):
                continue

            updated_time = time + graph[vertex][adj_vertex]

            if (distance[adj_vertex] > updated_time):
                distance[adj_vertex] = updated_time
                queue.append((updated_time, adj_vertex))

    if (answer < distance[-1]):
        answer = distance[-1]

print(answer)