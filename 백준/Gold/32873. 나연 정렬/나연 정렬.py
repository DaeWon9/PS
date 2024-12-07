import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS_ends = []

for num in A:
    idx = bisect_left(LIS_ends, num)
    if idx == len(LIS_ends):
        LIS_ends.append(num)
    else:
        LIS_ends[idx] = num

answer = len(LIS_ends)
print(answer)
