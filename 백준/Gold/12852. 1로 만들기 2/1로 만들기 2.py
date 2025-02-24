import sys
input = sys.stdin.readline

def solve(X):
    dp = [0] * (X + 1) 
    prev = [0] * (X + 1) 

    for i in range(2, X + 1):
        # 1을 빼는 경우
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1

        # 2로 나누는 경우
        if (i % 2 == 0 and dp[i // 2] + 1 < dp[i]):
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2

        # 3으로 나누는 경우
        if (i % 3 == 0 and dp[i // 3] + 1 < dp[i]):
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

    # 경로 추적
    path = []
    current = X
    while current != 0:
        path.append(current)
        current = prev[current]

    print(dp[X])
    print(*path)

X = int(input())
solve(X)
