import sys
input = sys.stdin.readline

N = int(input())
cost = []

for _ in range(N):
    cost.append(tuple(map(int, input().split())))

# row : N, col : 3
dp = [[[2147483647 for _ in range(3)] for _ in range(N)] for _ in range(3)]
answer = 2147483647

for case in range(3): # case0 : start R, case1 : start G, case2 : start B
    dp[case][0][case] = cost[0][case]
    for i in range(1, N):
        if (i == N - 1): # 마지막집은 0번째 집과도 비교
            if (case == 0): #R
                dp[case][i][1] = min(dp[case][i-1][0] + cost[i][1], dp[case][i-1][2] + cost[i][1])
                dp[case][i][2] = min(dp[case][i-1][0] + cost[i][2], dp[case][i-1][1] + cost[i][2])
            elif (case == 1): #G
                dp[case][i][0] = min(dp[case][i-1][1] + cost[i][0], dp[case][i-1][2] + cost[i][0])
                dp[case][i][2] = min(dp[case][i-1][0] + cost[i][2], dp[case][i-1][1] + cost[i][2])
            else: #B
                dp[case][i][0] = min(dp[case][i-1][1] + cost[i][0], dp[case][i-1][2] + cost[i][0])
                dp[case][i][1] = min(dp[case][i-1][0] + cost[i][1], dp[case][i-1][2] + cost[i][1])
        else:
            dp[case][i][0] = min(dp[case][i-1][1] + cost[i][0], dp[case][i-1][2] + cost[i][0])
            dp[case][i][1] = min(dp[case][i-1][0] + cost[i][1], dp[case][i-1][2] + cost[i][1])
            dp[case][i][2] = min(dp[case][i-1][0] + cost[i][2], dp[case][i-1][1] + cost[i][2])

    answer = min(answer, min(dp[case][N - 1]))

print(answer)