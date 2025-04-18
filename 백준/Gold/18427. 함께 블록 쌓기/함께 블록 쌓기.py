import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
dp = [[0 for _ in range(H+1)] for _ in range(N)] # dp[i번째 학생까지 놓았을때][높이별] = 개수

blocks = []

for _ in range(N):
    datas = list(map(int, input().split()))
    temp_list = []
    for data in datas:
        if (data <= H):
            temp_list.append(data)
    blocks.append(temp_list)

for block in blocks[0]:
    dp[0][block] = 1

for i in range(1, N):
    dp[i] = dp[i-1][:]
    for block in blocks[i]:
        dp[i][block] += 1
        for h in range(H, block-1, -1):
            dp[i][h] += dp[i-1][h-block]
            

print(dp[-1][-1] % 10007)