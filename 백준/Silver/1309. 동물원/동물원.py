import sys
input = sys.stdin.readline

n = int(input())

if (n == 1):
    print(3)
    exit(0)

dp = [0] * (n+1)
dp[1] = 2
dp[2] = 6
MOD = 9901

for i in range(3, n+1):
    dp[i] = (dp[i-1] * dp[1] + dp[i-2] + 2) % MOD

print((dp[n] + 1) % MOD)