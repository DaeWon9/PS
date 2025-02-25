import sys
input = sys.stdin.readline

N, M, K = map(int, input().split()) # 주문의 수 N(1 ≤ N ≤ 100), 치즈버거 개수 M(1 ≤ M ≤ 300), 감자튀김 개수 K(1 ≤ K ≤ 300

dp = [[0 for _ in range(K + 1)]for _ in range(M + 1)]

for _ in range(N):
    x, y = map(int, input().split())

    for c in range(M, x - 1, -1):
        for f in range(K, y - 1, -1):
            dp[c][f] = max(dp[c][f], dp[c - x][f - y] + 1)

print(dp[-1][-1])