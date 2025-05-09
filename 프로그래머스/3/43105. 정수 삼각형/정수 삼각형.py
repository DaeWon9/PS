def solution(triangle):
    N = len(triangle)
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for r in range(1, N+1):
        for c in range(r):
            dp[r][c] = max(dp[r][c], dp[r-1][c-1] + triangle[r-1][c], dp[r-1][c] + triangle[r-1][c])

    answer = max(dp[-1])
    return answer