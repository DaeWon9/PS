import sys
input = sys.stdin.readline

D, P = map(int, input().split())
dp = [0 for _ in range(D+1)] # dp[해당 길이일 때] = 최대 수도관 용량
dp[0] = float('inf')

for _ in range(P):
    l, c = map(int, input().split())
    for d in range(D, l-1, -1):
        dp[d] = max(dp[d], min(dp[d-l], c))

print(dp[-1])