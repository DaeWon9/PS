import sys
input = sys.stdin.readline

# k만큼의 카페인을 정확히 섭취하기 위한 최소 몇 개의 커피
# 냅색
INF = float('inf')
N, K = map(int, input().split())
dp = [INF] * (K+1) # k의 카페인을 섭취하기 위한 최소 커피 개수
C = list(map(int, input().split()))

if (K == 0):
    print(0)
    exit(0)

dp[0] = 0

for c in C:
    for k in range(K, c-1, -1):
        dp[k] = min(dp[k-c] + 1, dp[k])

if (dp[-1] == INF):
    print(-1)
else:
    print(dp[-1])
