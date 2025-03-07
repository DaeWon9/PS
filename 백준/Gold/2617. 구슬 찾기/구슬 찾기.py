import sys
input = sys.stdin.readline

INF = float('inf')
N, M = map(int, input().split())

mid_size = N // 2
answer = 0
connected = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    connected[u][v] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (connected[i][k] and connected[k][j]):
                connected[i][j] = 1

for i in range(1, N+1):
    big_count = 0
    small_count = 0
    for j in range(1, N+1):
        if (connected[i][j] == 1):
            small_count += 1
        if (connected[j][i] == 1):
            big_count +=1
    
    if (small_count > mid_size or big_count > mid_size):
        answer += 1

print(answer)