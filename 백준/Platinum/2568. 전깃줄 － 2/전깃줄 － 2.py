import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))

A.sort()
LIS = [A[0][1]]
memo = [(0, A[0][0])]
answer = []

for i in range(1, N):
    if (A[i][1] > LIS[-1]):
        LIS.append(A[i][1])
        memo.append((len(LIS) - 1, A[i][0]))
    else:
        idx = bisect_left(LIS, A[i][1])
        LIS[idx] = A[i][1]
        memo.append((idx, A[i][0]))

last_idx = len(LIS) - 1
for i in range(len(memo)-1, -1, -1):
    if (memo[i][0] == last_idx):
        last_idx -= 1
    else:
        answer.append(memo[i][1])

print(len(answer))
for A in answer[::-1]:
    print(A)