import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
M = int(input())
dp = [0 for _ in range(M+1)]

for l in range(N-1, -1, -1):
    pivot = P[l]
    for m in range(pivot, M+1):
        dp[m] = max(dp[m-pivot]*10+l, dp[m])

print(dp[m])