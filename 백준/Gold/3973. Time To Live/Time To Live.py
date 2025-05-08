import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, adj, N):
    visited = [-1] * N
    queue = deque()
    queue.append(start)
    visited[start] = 0
    farthest = (0, start)
    while queue:
        v = queue.popleft()
        for nv in adj[v]:
            if (visited[nv] == -1):
                visited[nv] = visited[v] + 1
                queue.append(nv)
                if (visited[nv] > farthest[0]):
                    farthest = (visited[nv], nv)
    return farthest

c = int(input())
for _ in range(c):
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    # 1. 임의의 노드(0)에서 가장 먼 노드 u 찾기
    _, u = bfs(0, adj, N)
    # 2. u에서 가장 먼 노드 v 찾기, 거리 d
    d, v = bfs(u, adj, N)
    # 3. 반지름 = (지름 + 1) // 2
    print((d + 1) // 2)