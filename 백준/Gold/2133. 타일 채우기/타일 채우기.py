import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 31
dp[2] = 3

for i in range(4, n+1, 2): 
    dp[i] = dp[i-2] * dp[2] # 2칸일때 나올 수 있는 개수만큼 곱해주고

    for j in range(4,i,2):
        dp[i] += dp[i-j] * 2 # 특이케이스가 새로 늘어난 칸에 의해 더 늘어남

    dp[i] += 2 # 특이케이스 2개씩

print(dp[n])