import sys
input = sys.stdin.readline

N = input().rstrip()

if N[0] == '0':
    print(0)
    exit(0)

dp = [0] * (len(N) + 1)
dp[0] = 1
dp[1] = 1 

MOD = 1000000

for i in range(2, len(N) + 1):
    if (N[i - 1] != '0'):
        dp[i] += dp[i - 1]
        dp[i] %= MOD

    two_digit = int(N[i - 2:i])
    if (10 <= two_digit <= 26):
        dp[i] += dp[i - 2]
        dp[i] %= MOD

print(dp[-1])
