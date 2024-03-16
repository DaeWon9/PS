import sys
input = sys.stdin.readline

def find(r, c):
    while True:
        if (prev_path[r][c] == prev_path[r][prev_path[r][c]]):
            return prev_path[r][c]
        else:
            prev_path[r][c] = prev_path[r][prev_path[r][c]]

n, m = map(int, input().split())
graph = [[2147483647 for _ in range(n + 1)] for _ in range(n + 1)]
prev_path = [['-' for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1][v2] = cost
    graph[v2][v1] = cost
    prev_path[v1][v2] = v2
    prev_path[v2][v1] = v1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (graph[i][j] > graph[i][k] + graph[k][j]):
                prev_path[i][j] = k
                graph[i][j] = graph[i][k] + graph[k][j]
                
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if (prev_path[r][c] == '-'):
            print('-', end = ' ')
        else:
            print(find(r, c), end = ' ')
    print()