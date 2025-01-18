import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0] = [0] + [1 for _ in range(K)]

for n in range(1, N+1):
    for k in range(1, K+1):
        dp[n][k] = dp[n-1][k] + dp[n][k-1]

print(dp[N][K] % 1_000_000_000)