import sys
input = sys.stdin.readline

INF = 2147483647
N, M = map(int, input().split())
infos = [[0, 0] for _ in range(N)]  # 메모리, 비용

summed_memory = 0
for j, data in enumerate(map(int, input().split())):
    infos[j][0] = data
    summed_memory += data

for j, data in enumerate(map(int, input().split())):
    infos[j][1] = data

max_m = M + summed_memory
dp = [INF] * (max_m + 1)  # dp[메모리] = 최소 비용
dp[0] = 0 

for m, c in infos:
    for target_m in range(max_m, m - 1, -1):
        dp[target_m] = min(dp[target_m], dp[target_m - m] + c)

print(min(dp[M:]))
