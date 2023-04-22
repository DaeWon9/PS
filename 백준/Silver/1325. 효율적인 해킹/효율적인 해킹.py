import sys
from collections import deque, defaultdict

def bfs(graph, start, visited):
    global result

    queue = deque([start])
    visited[start] = True

    while queue:
        result += 1
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

computer_count, edge_count = map(int, sys.stdin.readline().rstrip().split())
graph = defaultdict(list)
result_list = []
max_count = 0

for _ in range(edge_count):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[b] += [a]

for i in range(1, computer_count + 1):
    visited = [False] * (computer_count + 1)
    result = 0
    bfs(graph, i, visited)
    result_list.append([i, result])
    max_count = max(max_count, result)

result_list.sort(key = lambda x :(x[1]), reverse=True)

for data in result_list:
    if (data[1] == max_count):
        print(data[0], end=' ')
    else:
        break
