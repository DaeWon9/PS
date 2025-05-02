import sys
input = sys.stdin.readline

def get_area_sum(l, r):
    if (l > r):
        l, r = r, l
    
    if (l == 0):
        return summed_arr[r]

    return summed_arr[r] - summed_arr[l-1]

# 제한시간 1초
N = int(input()) # 50000 이하
arr = list(map(int, input().split()))
K = int(input())

summed_arr = [0 for _ in range(N)]
summed_arr[0] = arr[0]

for i in range(1, N):
    summed_arr[i] += summed_arr[i-1] + arr[i]

# dp[i개의 소형 기관차를 사용][j번 열차까지] = 최대 수
dp = [[0 for _ in range(N)] for _ in range(4)]

for i in range(1, 4):
    for j in range(i * K - 1, N):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - K] + get_area_sum(j - K + 1, j))

print(dp[-1][-1])