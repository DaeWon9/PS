import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

indegree = [0 for _ in range(N + 1)]
adj_vertices = [[] for _ in range(N + 1)]
need_count_list = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

basic_part_set = set()
queue = deque()

for _ in range(M):
    origin, sub, count = map(int, input().split())
    indegree[origin] += 1
    need_count_list[origin][sub] = count
    adj_vertices[sub].append((origin, count))

for v in range(1, N + 1):
    if (indegree[v] == 0):
        queue.append(v)
        basic_part_set.add(v)

while queue:
    v = queue.popleft()

    for next, count in adj_vertices[v]:
        indegree[next] -= 1

        if (v not in basic_part_set):
            for index in range(1, N + 1):
                if (need_count_list[v][index] == 0):
                    continue
                need_count_list[next][index] += count * need_count_list[v][index]
        
        if (indegree[next] == 0):
            queue.append(next)

for id in range(1, N + 1):
    if (id in basic_part_set):
        print(id, need_count_list[N][id])