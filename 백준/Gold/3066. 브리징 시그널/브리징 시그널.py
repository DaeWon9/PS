import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input()) # 1 ≤ N ≤ 40000

    port_nums = []
    for _ in range(N):
        port_nums.append(int(input()))
    
    LIS = [port_nums[0]]

    for i in range(1, N):
        target_port = port_nums[i]
        if (LIS[-1] < target_port):
            LIS.append(target_port)
        else:
            idx = bisect_left(LIS, target_port)
            LIS[idx] = target_port
    
    print(len(LIS))