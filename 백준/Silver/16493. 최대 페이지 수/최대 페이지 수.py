import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0] * (N+1)

for _ in range(M):
    day, page = map(int, input().split())

    for d in range(N, day-1, -1):
        dp[d] = max(dp[d-day] + page, dp[d])

print(dp[-1])