import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
str3 = input().rstrip()

N = len(str1)
M = len(str2)
K = len(str3)

dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(1, K+1):
            if (str1[i-1] == str2[j-1] == str3[k-1]):
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])