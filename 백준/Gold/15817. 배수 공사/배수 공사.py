import sys
input = sys.stdin.readline

N, X = map(int, input().split())
dp = [0] * (X+1)
dp[0] = 1

for _ in range(N):
    L, C = map(int, input().split())

    for x in range(X, -1, -1):
        for c in range(1, C+1):
            if (x-c*L < 0):
                break
            dp[x] += dp[x-c*L]
            
print(dp[X])