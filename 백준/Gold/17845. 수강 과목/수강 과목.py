import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0 for _ in range(N+1)] # dp[i시간 공부할 때] = 최대 중요도

for _ in range(K):
    i, t = map(int, input().split())

    for tt in range(N, t-1, -1):
        dp[tt] = max(dp[tt-t] + i, dp[tt])

print(dp[-1])