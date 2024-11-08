import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    num_list = list(map(int, input().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(K-1):
        dp[i][i+1] = num_list[i] + num_list[i+1]

    # dp[0][K] = min([dp[0][2] + dp[3][K], dp[0][3] + dp[4][K], dp[0][N] + dp[N+1][K]])
    for i in range(K-1, -1, -1):
        for j in range(i+1, K):
            min_value = 2147483647
            
            for k in range(i, j):
                value = dp[i][k] + dp[k+1][j]

                if (min_value > value):
                    min_value = value

            dp[i][j] = min_value + sum(num_list[i:j+1])
    
    print(dp[0][-1])