import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]
memo = [(0, A[0])]
answer = []

for i in range(1, N):
    if (LIS[-1] < A[i]):
        LIS.append(A[i])
        memo.append((len(LIS) - 1, A[i]))
    else:
        idx = bisect_left(LIS, A[i])
        LIS[idx] = A[i]
        memo.append((idx, A[i]))

last_idx = len(LIS) - 1

for idx, num in memo[::-1]:
    if (last_idx == idx):
        answer.append(num)
        last_idx -= 1

print(len(LIS))
for num in answer[::-1]:
    print(num, end=' ')
