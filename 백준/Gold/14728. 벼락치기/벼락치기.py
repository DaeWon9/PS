import sys
input = sys.stdin.readline

N, T = map(int, input().split())
dp = [0] * (T+1) # dp[시간] = 최대점수

for _ in range(N):
    k, s = map(int, input().split())

    for t in range(T, k-1, -1):
        dp[t] = max(dp[t-k] + s, dp[t])

print(dp[-1])