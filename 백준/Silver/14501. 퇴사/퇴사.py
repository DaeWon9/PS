import sys

N = int(sys.stdin.readline())

schedule_list = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    schedule_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(i+schedule_list[i][0], N+1):
        if (dp[j] < dp[i] + schedule_list[i][1]):
            dp[j] = dp[i] + schedule_list[i][1]


print(dp[-1])