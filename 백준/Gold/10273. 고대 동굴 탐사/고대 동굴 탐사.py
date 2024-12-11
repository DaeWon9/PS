import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 최대의 이득을 내는 정점을 찾는다.
# 해당 정점으로 부터 이득이 최대가 되는 경로를 역추적한다.
# dp에 저장되어있는 최대의 이득을 가지는 edge를 따라서 root 까지 간다.

T = int(input())

for _ in range(T):
    N, E = map(int, input().split())
    L = list(map(int, input().split()))

    adj_vertices = defaultdict(list)
    reversed_adj_vertices = defaultdict(list)
    indegree = defaultdict(int)
    queue = deque()
    dp = [-2147483647] * N
    dp[0] = L[0]

    for __ in range(E):
        a, b, c = map(int, input().split()) # a -> b
        a -= 1
        b -= 1
        
        adj_vertices[a].append((b, L[b] - c))
        reversed_adj_vertices[b].append((a, L[b] - c))
        indegree[b] += 1

    queue.append((L[0], 0))

    while queue:
        l, v = queue.popleft()

        for adj_vertex, ll in adj_vertices[v]:
            updated_l = l + ll

            if (dp[adj_vertex] < updated_l):
                dp[adj_vertex] = updated_l

            indegree[adj_vertex] -= 1

            if (indegree[adj_vertex] == 0):
                queue.append((dp[adj_vertex], adj_vertex))

    goal = 0
    max_l = dp[0]
    for i in range(1, N):
        if (max_l < dp[i]):
            goal = i
            max_l = dp[i]

    path = [goal]
    queue.append((dp[goal], goal))

    while queue:
        l, v = queue.popleft()

        for adj_vertex, ll in reversed_adj_vertices[v]:
            prev_l = l - ll

            if (dp[adj_vertex] == prev_l):
                path.append(adj_vertex)
                queue.append((prev_l, adj_vertex))
                break

    print(max_l, len(path))
    for i in range(len(path)-1, -1, -1):
        print(path[i] + 1, end = ' ')