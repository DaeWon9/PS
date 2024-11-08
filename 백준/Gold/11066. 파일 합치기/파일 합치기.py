import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    num_list = list(map(int, input().split()))
    
    prefix_sum = [0] * (K + 1)
    for i in range(K):
        prefix_sum[i+1] = prefix_sum[i] + num_list[i]
    
    dp = [[0] * K for _ in range(K)]
    opt = [[0] * K for _ in range(K)]
    
    for i in range(K-1):
        dp[i][i+1] = num_list[i] + num_list[i+1]
        opt[i][i+1] = i
    
    for length in range(2, K):
        for i in range(K - length):
            j = i + length
            dp[i][j] = 2147483647
            start = opt[i][j-1]
            end = opt[i+1][j] if (j < K) else j-1
            for k in range(start, end + 1):
                cost = dp[i][k] + dp[k+1][j] + prefix_sum[j+1] - prefix_sum[i]
                if (cost < dp[i][j]):
                    dp[i][j] = cost
                    opt[i][j] = k
    
    print(dp[0][K-1])
