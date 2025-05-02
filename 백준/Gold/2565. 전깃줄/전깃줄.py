import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(501)]
LIS = []

for _ in range(N):
    u, v = map(int, input().split())
    
    arr[v] = u

for i in range(501):
    if (arr[i] == 0):
        continue

    if (not LIS):
        LIS.append(arr[i])
        continue

    if (LIS[-1] < arr[i]):
        LIS.append(arr[i])
    else:
        idx = bisect_left(LIS, arr[i])
        LIS[idx] = arr[i]

print(N - len(LIS))