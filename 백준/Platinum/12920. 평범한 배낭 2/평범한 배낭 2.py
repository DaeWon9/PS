import sys
input = sys.stdin.readline

item_count, max_weight = map(int, input().split())
item_list = []

for _ in range(item_count):
    weight, value, count = map(int, input().split())

    mutilplied_value = 1

    while (count > 0):
        if (count < mutilplied_value):
            mutilplied_value = count
        item_list.append((weight * mutilplied_value, value * mutilplied_value))

        count -= mutilplied_value
        mutilplied_value *= 2

dp = [[0 for _ in range(max_weight + 1)] for _ in range(len(item_list) + 1)]

for row in range(1, len(item_list) + 1):
    weight, value = item_list[row - 1]
    for col in range(1, max_weight + 1):
        if (col >= weight):
            dp[row][col] = max(dp[row - 1][col], dp[row - 1][col - weight] + value)
        else:
            dp[row][col] = dp[row - 1][col]

print(dp[-1][-1])