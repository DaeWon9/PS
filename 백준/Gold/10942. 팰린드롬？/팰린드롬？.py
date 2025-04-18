import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 0: not visited
# 1: False, 2: True

def is_palindrome(s, e):    
    if (dp[s][e] != 0):
        return dp[s][e]
    
    if (arr[s] == arr[e] and is_palindrome(s+1, e-1) == 2):
        dp[s][e] = 2
    else:
        dp[s][e] = 1

    return dp[s][e]


N = int(input())
arr = list(map(str, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 2 # 숫자 한개는 팰린드롬임.

    if (i+1 < N and arr[i] == arr[i+1]):
        dp[i][i+1] = 2

M = int(input())

for _ in range(M):
    S, E = map(int, input().split())

    if (is_palindrome(S-1, E-1) == 1):
        print(0)
    else:
        print(1)