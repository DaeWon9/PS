import sys
from bisect import bisect_left
input = sys.stdin.readline

# 증가하는 수열
N = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]

for i in range(1, N):
    if (LIS[-1] < arr[i]):
        LIS.append(arr[i])
    else:
        idx = bisect_left(LIS, arr[i])
        LIS[idx] = arr[i]

print(N - len(LIS))