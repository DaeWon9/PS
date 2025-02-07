import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    LIS = [arr[0]]
    memo = [(0, 0)]

    for i in range(1, N):
        if (LIS[-1] < arr[i]):
            LIS.append(arr[i])
            memo.append((len(LIS)-1, i))
        else:
            idx = bisect_left(LIS, arr[i])
            LIS[idx] = arr[i]
            memo.append((idx, i))

    last_idx = len(LIS) - 1
    path = []

    for i in range(len(memo)-1, -1, -1):
        if (memo[i][0] == last_idx):
            path.append(memo[i][1] + 1)
            last_idx -= 1

    print(len(LIS))
    print(*path[::-1])