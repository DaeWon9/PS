import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
indegree = defaultdict(int)
adj_vertices = defaultdict(list)
answer_set = set()
visited = [False for _ in range(N+1)]


for v in range(1, N+1):
    v1, v2 = map(int, input().split())

    adj_vertices[v].append(v1)
    adj_vertices[v].append(v2)

    indegree[v1] += 1
    indegree[v2] += 1

while True:
    flag = False
    for v in range(1, N+1):
        if (visited[v]): 
            continue

        if (indegree[v] < 2):
            visited[v] = True
            flag = True
            for adj_vertex in adj_vertices[v]:
                indegree[adj_vertex] -= 1
    
    if (not flag):
        break

for v in range(1, N+1):
    if (indegree[v] == 2):
        answer_set.add(v)

print(len(answer_set))
print(*sorted(answer_set))