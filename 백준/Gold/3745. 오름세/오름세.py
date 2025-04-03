import sys
from bisect import bisect_left
input = sys.stdin.readline

while True:
    try:
        N = int(input())
    except:
        break

    arr = list(map(int, input().split()))

    LIS = [arr[0]]

    for i in range(1, N):
        if (LIS[-1] < arr[i]):
            LIS.append(arr[i])
        else:
            idx = bisect_left(LIS, arr[i])
            LIS[idx] = arr[i] 
    
    print(len(LIS))