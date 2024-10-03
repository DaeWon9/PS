import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))
num_list.sort()

sum_list = { x + y for x, y in combinations_with_replacement(num_list, 2)}

for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if (num_list[i] - num_list[j] in sum_list): 
            print(num_list[i])
            exit(0)