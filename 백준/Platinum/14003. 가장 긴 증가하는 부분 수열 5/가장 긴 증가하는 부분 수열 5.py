import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]
memo = [(0, A[0])] 

for i in range(1, N):
    if (A[i] > LIS[-1]):
        LIS.append(A[i])
        memo.append((len(LIS)-1, A[i]))
    else:
        idx = bisect_left(LIS, A[i])
        LIS[idx] = A[i]
        memo.append((idx, A[i]))
        
last_idx = len(LIS) - 1
res = []

for i in range(len(memo)-1, -1, -1):
    if (memo[i][0] == last_idx):
        res.append(memo[i][1])
        last_idx -= 1

print(len(LIS))
print(*res[::-1])