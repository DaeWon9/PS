import sys
input = sys.stdin.readline

C, N = map(int, input().split())

info_list = []
for _ in range(N):
    a, b = map(int, input().split()) # a원을 투자하여 b명의 고객을 얻음
    info_list.append((a, b))

dp = [777777777 for _ in range(1101)] # m명 구할때 필요한 금액
dp[0] = 0

for m in range(1, 1101):
    for a, b in info_list:
        if (m-b < 0):
            continue
        
        dp[m] = min(dp[m-b] + a, dp[m])

print(min(dp[C:]))