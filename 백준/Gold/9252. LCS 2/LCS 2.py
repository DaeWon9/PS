import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

N = len(str1)
M = len(str2)
LCS = ""
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if (str1[i-1] == str2[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
i = N
j = M
while (i > 0 and j > 0):
    if (str1[i-1] == str2[j-1]):
        LCS += str1[i-1]
        i -= 1
        j -= 1
    else:
        left = dp[i][j-1]
        top = dp[i-1][j]

        if (left < top):
            i -= 1
        else:
            j -= 1

print(dp[-1][-1])
print(LCS[::-1])