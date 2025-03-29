import sys
from bisect import bisect_left
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    input_data = list(map(int, input().split()))
    case_num, arr = input_data[0], input_data[1:]

    temp = []
    answer = 0

    for i, num in enumerate(arr):
        target_idx = bisect_left(temp, num)
        temp.append(num)
        answer += (i - target_idx)
        
        if (target_idx != i):
            temp.sort()
    
    print(case_num, answer)