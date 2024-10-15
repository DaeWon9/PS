import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]

for i in range(1, N):
    if (arr[i] > LIS[-1]):
        LIS.append(arr[i])
    else:
        idx = bisect_left(LIS, arr[i])
        LIS[idx] = arr[i]

print(N - len(LIS))