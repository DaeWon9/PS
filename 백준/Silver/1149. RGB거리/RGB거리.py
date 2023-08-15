import sys

n = int(sys.stdin.readline())

cost = []

for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * 3 for _ in range(n + 1)]

dp[1] = cost[0]

for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i - 1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i - 1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i - 1][2]

print(min(dp[-1]))
