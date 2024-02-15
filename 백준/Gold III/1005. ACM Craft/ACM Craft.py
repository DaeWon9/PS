import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(N, construction_time_list, adj_vertices, indegree, target_vertex):
    time = [0 for _ in range(N + 1)]
    queue = deque()

    for vertex in range(1, N+1):
        if (indegree[vertex] == 0):
            queue.append(vertex)
            time[vertex] += construction_time_list[vertex - 1]

    while queue:
        v = queue.popleft()

        for vertex in adj_vertices[v]:
            indegree[vertex] -= 1
            time[vertex] = max(time[vertex], time[v] + construction_time_list[vertex - 1])

            if (indegree[vertex] == 0):
                queue.append(vertex)

    print(time[target_vertex])


test_case = int(input())

for _ in range(test_case):
    N, K = map(int, input().split())
    construction_time_list = list(map(int, input().split()))

    adj_vertices = defaultdict(list)
    indegree = defaultdict(int)

    for _ in range(K):
        v1, v2 = map(int, input().split())
        adj_vertices[v1].append(v2)
        indegree[v2] += 1

    target_vertex = int(input())

    solution(N, construction_time_list, adj_vertices, indegree, target_vertex)