import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    
    # dp[mod] = 최대 기타 개수
    dp = [-1] * M
    dp[0] = 0

    for num in S:
        new_dp = dp[:]
        for mod in range(M):
            if dp[mod] != -1:
                new_mod = (mod + num) % M
                new_dp[new_mod] = max(new_dp[new_mod], dp[mod] + 1)
        dp = new_dp

    print(dp[0])
