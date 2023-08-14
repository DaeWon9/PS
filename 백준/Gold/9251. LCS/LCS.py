import sys

array_1 = sys.stdin.readline().rstrip()
array_2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(array_2) + 1) for _ in range(len(array_1) + 1)]

for i in range(1, len(array_1) + 1):
    for j in range(1, len(array_2) + 1):
        if array_1[i - 1] == array_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])