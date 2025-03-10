import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[2147483647 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    v1, v2, case = map(int, input().split())
    graph[v1][v2] = 0
    if (case == 1): # 양방향
        graph[v2][v1] = 0
    else:
        graph[v2][v1] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (graph[i][j] > graph[i][k] + graph[k][j]):
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n + 1):
    graph[i][i] = 0

k = int(input())
for _ in range(k):
    start, end = map(int, input().split())
    print(graph[start][end])