import sys

item_count, max_weight = map(int, sys.stdin.readline().split())

dp = [[0] * (max_weight + 1) for _ in range(item_count + 1)]
items = [[0, 0]]

for _ in range(item_count):
    items.append(list(map(int, input().split())))

for i in range(1, item_count + 1):
    for j in range(1, max_weight + 1):
        weight, value = items[i]
        if j >= weight:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])