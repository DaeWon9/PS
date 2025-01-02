import sys
input = sys.stdin.readline

T, W = map(int, input().split())
dp = [[0 for _ in range(2)] for _ in range(W + 1)]

for i in range(T):
    target = int(input()) - 1

    for n in range(W+1):
        if (n == 0 and target == 0):
            dp[0][0] += 1
            continue

        cur_pos = n % 2
        if (target == cur_pos):
            dp[n][cur_pos] = max(dp[n-1][1-cur_pos] + 1, dp[n][cur_pos] + 1)
        else:
            dp[n][target] = max(dp[n-1][1-cur_pos], dp[n][cur_pos])
answer = 0
for d in dp:
    answer = max(answer, d[0], d[1])
print(answer)
