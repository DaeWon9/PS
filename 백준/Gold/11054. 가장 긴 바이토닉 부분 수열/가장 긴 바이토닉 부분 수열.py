import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
reversed_arr = arr[:]
reversed_arr.reverse()
increase = [[0, 0] for _ in range(N)]
decrease = [[0, 0] for _ in range(N)]
increase[0] = [1, arr[0]]
decrease[0] = [1, reversed_arr[0]]

LIS = [arr[0]]
RLIS = [reversed_arr[0]]
answer = 0

for i in range(1, N):
    if (LIS[-1] < arr[i]):
        LIS.append(arr[i])
        increase[i] = [len(LIS), arr[i]]
    else:
        idx = bisect_left(LIS, arr[i])
        LIS[idx] = arr[i]
        increase[i] = increase[i-1]

    if (RLIS[-1] < reversed_arr[i]):
        RLIS.append(reversed_arr[i])
        decrease[i] = [len(RLIS), reversed_arr[i]]
    else:
        idx = bisect_left(RLIS, reversed_arr[i])
        RLIS[idx] = reversed_arr[i]
        decrease[i] = decrease[i-1]

for i in range(N):
    increase_value = increase[i]
    decrease_value = decrease[N-i-1]

    len_sum = increase_value[0] + decrease_value[0]

    if (increase_value[1] == decrease_value[1]):
        len_sum -= 1

    if (answer < len_sum):
        answer = len_sum
    
print(answer)