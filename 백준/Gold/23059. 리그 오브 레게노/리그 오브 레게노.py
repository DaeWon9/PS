import sys
from collections import deque, defaultdict

input = sys.stdin.readline
adj_vertices = defaultdict(list)
indegree = defaultdict(int)

max_group_dict = defaultdict(int)
item_set = set()
queue = deque()
answer = []

group = 0

N = int(input())
for _ in range(N):
    prev, next = map(str, input().rstrip().split())

    adj_vertices[prev].append(next)
    indegree[next] += 1

    item_set.add(prev)
    item_set.add(next)

for item in item_set:
    if (indegree[item] == 0):
        answer.append((group, item))
        queue.append((group, item))

while queue:
    g, v = queue.popleft()

    for adj_vertex in adj_vertices[v]:
        indegree[adj_vertex] -= 1
        max_group_dict[adj_vertex] = max(max_group_dict[adj_vertex], g + 1)

        if (indegree[adj_vertex] == 0):
            answer.append((max_group_dict[adj_vertex], adj_vertex))
            queue.append((max_group_dict[adj_vertex], adj_vertex))

answer.sort(key= lambda x : (x[0], x[1]))

if (len(item_set) != len(answer)):
    print(-1)
    exit(0)

for ans in answer:
    print(ans[1])