import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

MOD = 1_000_000_003

def solve(dp, n, k):
    if k == 0:
        return 1
    if n < k:
        return 0
    if dp[n][k] != -1:
        return dp[n][k]

    dp[n][k] = (solve(dp, n - 1, k) + solve(dp, n - 2, k - 1)) % MOD
    return dp[n][k]

N = int(input())
K = int(input())

if K > (N + 1) // 2:
    print(0)
    exit(0)

dp1 = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]
dp2 = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]

# 첫 번째 색상을 선택한 경우
case1 = solve(dp1, N - 3, K - 1)
# 첫 번째 색상을 선택하지 않은 경우
case2 = solve(dp2, N - 1, K)

print((case1 + case2) % MOD)
