import sys
from collections import deque
input = sys.stdin.readline

def bfs(vertices, start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        cnt += 1

        for adj_vertex in vertices[v]:
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                queue.append(adj_vertex)

    return cnt

N, M, X = map(int, input().split())

adj_vertices = [[] for _ in range(N + 1)]
reversed_adj_vertices = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_vertices[u].append(v)
    reversed_adj_vertices[v].append(u)

next_cnt = bfs(adj_vertices, X)
prev_cnt = bfs(reversed_adj_vertices, X)

U = prev_cnt
V = N - next_cnt + 1

print(U, V)
