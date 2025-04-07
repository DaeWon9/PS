import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input()) # 1 ≤ N ≤ 40000
port_nums = list(map(int, input().split()))
LIS = [port_nums[0]]

for i in range(1, N):
    target_port = port_nums[i]
    if (LIS[-1] < target_port):
        LIS.append(target_port)
    else:
        idx = bisect_left(LIS, target_port)
        LIS[idx] = target_port

print(len(LIS))