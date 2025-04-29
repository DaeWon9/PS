import sys
input = sys.stdin.readline

# 열린문은 항상 두개..

def solve(idx, open1, open2):
    if (idx == M):
        return 0
    
    if (dp[idx][open1][open2] != -1):
        return dp[idx][open1][open2]
    
    target = nums[idx]
    
    # 이미 열려있는 경우
    if (target == open1 or target == open2):
        dp[idx][open1][open2] = solve(idx + 1, open1, open2)
        return dp[idx][open1][open2]
    
    move1 = abs(target - open1) + solve(idx + 1, target, open2)
    move2 = abs(target - open2) + solve(idx + 1, open1, target)
    
    dp[idx][open1][open2] = min(move1, move2)
    return dp[idx][open1][open2]

N = int(input())
O1, O2 = map(int, input().split())
M = int(input())
nums = [int(input()) for _ in range(M)]

# dp[idx까지][open1][open2] = 최소 이동 횟수
dp = [[[-1] * (N+1) for _ in range(N+1)] for _ in range(M+1)]
print(solve(0, O1, O2))