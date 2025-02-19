import sys
input = sys.stdin.readline

H, N = map(int, input().split()) # H: 목표 키의 합
dp = [0] * (H+1) # min중에 max
datas = []
for _ in range(N):
    height, speed = map(int, input().split())
    datas.append((height, speed))


for h, s in datas:
    for target_h in range(H, h-1, -1):        
        if (target_h == h):
            dp[target_h] = max(dp[target_h], s)
            continue

        dp[target_h] = max(dp[target_h], min(dp[target_h-h], s))

print(dp[-1])