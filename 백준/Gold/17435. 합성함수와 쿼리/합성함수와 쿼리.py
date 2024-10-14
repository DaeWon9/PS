import sys
input = sys.stdin.readline

# 2^18 > 200,000
log = 18
m = int(input())
f = [0] + list(map(int,input().split()))
dp = [[f[i]] for i in range(m + 1)]

for j in range(1, log + 1):
    for i in range(1, m + 1):
        dp[i].append(dp[dp[i][j-1]][j-1])

Q = int(input())
for _ in range(Q):
    n, x = map(int, input().split())
    for b in range(log, -1, -1):
        if (n >= 1 << b):
            n -= 1 << b
            x = dp[x][b]
    print(x)