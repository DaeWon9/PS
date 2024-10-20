import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
m = int(input())

adj_vertices = defaultdict(list)
reversed_adj_vertices = defaultdict(list)
in_degree = [0 for _ in range(n + 1)]
queue = deque()

time = [0 for _ in range(n + 1)]
path_set = set()

for _ in range(m):
    v1, v2, t = map(int, input().split())
    adj_vertices[v1].append((v2, t))
    reversed_adj_vertices[v2].append((v1, t))

    in_degree[v2] += 1

start, end = map(int, input().split())
queue.append(start)

while queue:
    v = queue.popleft()

    for adj_vertex, t in adj_vertices[v]:
        in_degree[adj_vertex] -= 1
        
        updated_time = t + time[v]
        if (time[adj_vertex] < updated_time):
            time[adj_vertex] = updated_time

        if (in_degree[adj_vertex] == 0):
            queue.append(adj_vertex)

visited = [False for _ in range(n + 1)]
queue.append(end)
while queue:
    v = queue.pop()
    
    for adj_vertex, t in reversed_adj_vertices[v]:
        target_time = time[v] - time[adj_vertex]

        if (target_time == t):
            path_set.add((v, adj_vertex))

            if (not visited[adj_vertex]):
                queue.append(adj_vertex)
                visited[adj_vertex] = True

print(time[end])
print(len(path_set))