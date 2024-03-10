import sys
input = sys.stdin.readline
# 모든 지역간의 최단거리를 구해야함 & n = 100 일떄 n^3 = 100만 -> 플로이드-워셜

n, m, r = map(int, input().split())
item_count = list(map(int, input().split()))
answer = 0

graph = [[2147483647 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(r):
    v1, v2, distance = map(int, input().split())
    if (graph[v1][v2] > distance):
        graph[v1][v2] = distance
        graph[v2][v1] = distance

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in range(1, n + 1):
    sum = 0
    for col in range(1, n + 1):
        if (graph[row][col] <= m):
            sum += item_count[col - 1]
    answer = max(answer, sum)

print(answer)