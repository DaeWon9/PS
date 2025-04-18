import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))  # 오름차순
    M = int(input())

    dp = [[0 for _ in range(M+1)] for _ in range(N)]

    for i in range(N):
        coin = arr[i]

        if (coin <= M):
            dp[i][coin] = 1

        for j in range(1, M+1):
            if (i > 0):
                dp[i][j] += dp[i-1][j]
            if (j >= coin):
                dp[i][j] += dp[i][j - coin]

    print(dp[-1][-1])