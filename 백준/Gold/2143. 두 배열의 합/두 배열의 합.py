import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_count_dict = defaultdict(int)
B_count_dict = defaultdict(int)

A_count_dict[A[0]] += 1
B_count_dict[B[0]] += 1
summed_area_A = [A[0]]
summed_area_B = [B[0]]

for i in range(1, n):
    A_count_dict[A[i]] += 1
    summed_area_A.append(summed_area_A[-1] + A[i])

for i in range(1, m):
    B_count_dict[B[i]] += 1
    summed_area_B.append(summed_area_B[-1] + B[i])

for set_len in range(2, n+1):
    for i in range(set_len-1, n):
        if (i == set_len-1):
            A_count_dict[summed_area_A[i]] += 1
        else:
            A_count_dict[summed_area_A[i] - summed_area_A[i-set_len]] += 1

for set_len in range(2, m+1):
    for i in range(set_len-1, m):
        if (i == set_len-1):
            B_count_dict[summed_area_B[i]] += 1
        else:
            B_count_dict[summed_area_B[i] - summed_area_B[i-set_len]] += 1

answer = 0
for A_key in A_count_dict.keys():
    B_key = T - A_key

    if (B_key in B_count_dict):
        answer += A_count_dict[A_key] * B_count_dict[B_key]

print(answer)