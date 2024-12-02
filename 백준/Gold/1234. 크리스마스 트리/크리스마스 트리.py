import sys
input = sys.stdin.readline

def solve(N, R, G, B):
    if (N == 0):
        return 1

    if (dp[N][R][G][B] != -1):
        return dp[N][R][G][B]

    dp[N][R][G][B] = 0

    if (N % 3 == 0):
        D_N = N // 3
        if (R >= D_N and G >= D_N and B >= D_N):
            dp[N][R][G][B] += (fact[N] // (fact[D_N] * fact[D_N] * fact[D_N]) *
                                solve(N - 1, R - D_N, G - D_N, B - D_N))
    if (N % 2 == 0):
        D_N = N // 2
        if (R >= D_N and G >= D_N): # RG
            dp[N][R][G][B] += (fact[N] // (fact[D_N] * fact[D_N]) *
                                solve(N - 1, R - D_N, G - D_N, B))
        if (G >= D_N and B >= D_N): # GB
            dp[N][R][G][B] += (fact[N] // (fact[D_N] * fact[D_N]) *
                                solve(N - 1, R, G - D_N, B - D_N))
        if (R >= D_N and B >= D_N): # RB
            dp[N][R][G][B] += (fact[N] // (fact[D_N] * fact[D_N]) *
                                solve(N - 1, R - D_N, G, B - D_N))
    if (N <= R):
        dp[N][R][G][B] += solve(N - 1, R - N, G, B)
    if (N <= G):
        dp[N][R][G][B] += solve(N - 1, R, G - N, B)
    if (N <= B):
        dp[N][R][G][B] += solve(N - 1, R, G, B - N)

    return dp[N][R][G][B]

N, R, G, B = map(int, input().split())
dp = [[[[-1 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)] for _ in range(11)]
fact = [1] * 11
for i in range(1, 11):
    fact[i] = fact[i - 1] * i
    
print(solve(N, R, G, B))