import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[2147483647 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
    
path = [[[r] for _ in range(n + 1)] for r in range(n + 1)]

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    if (graph[v1][v2] > cost):
        graph[v1][v2] = cost

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (graph[i][j] > graph[i][k] + graph[k][j]):
                path[i][j] = path[i][k] + path[k][j]
                graph[i][j] = graph[i][k] + graph[k][j]

for r in range(1, n + 1):
    for c in range(1, n + 1):
        if (graph[r][c] == 2147483647):
            print(0)
        else:
            print(graph[r][c])
    
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if (r == c or graph[r][c] == 2147483647):
            print(0)
        else:
            print(len(path[r][c]) + 1, *path[r][c] , c)