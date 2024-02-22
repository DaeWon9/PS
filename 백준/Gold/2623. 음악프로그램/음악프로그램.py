import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = defaultdict(int)
adj_vertices = defaultdict(list)
queue = deque()
answer = []

for _ in range(M):
    order_list = list(map(int, input().split()))

    for i in range(1, order_list[0]):
        adj_vertices[order_list[i]].append(order_list[i + 1])
        indegree[order_list[i + 1]] += 1

for id in range(1, N + 1):
    if (indegree[id] == 0):
        queue.append(id)

while queue:
    v = queue.popleft()
    answer.append(v)

    for vertex in adj_vertices[v]:
        indegree[vertex] -= 1
        if (indegree[vertex] == 0):
            queue.append(vertex)

if (len(answer) != N):
    print(0)
else:
    for singer in answer:
        print(singer)