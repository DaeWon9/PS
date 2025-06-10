import sys
input = sys.stdin.readline

n, k = map(int, input().split())
distance = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for _ in range(k):
    u, v = map(int, input().split()) # u가 v보다 먼저 일어남
    distance[u][v] = 1

for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (distance[i][j] > distance[i][k] + distance[k][j]):
                distance[i][j] = distance[i][k] + distance[k][j]

s = int(input())
for _ in range(s):
    # u의 사건이 먼저 일어났으면 -1, 아니면 1, 모르면 0
    u, v = map(int, input().split()) 

    if (distance[u][v] != float('inf')):
        print(-1)
    elif (distance[v][u] != float('inf')):
        print(1)
    else:
        print(0)