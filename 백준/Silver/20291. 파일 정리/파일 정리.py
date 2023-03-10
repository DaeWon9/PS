import sys
from collections import Counter

N = int(sys.stdin.readline())

file_list = []

for _ in range(N):
    file_list.append(sys.stdin.readline().rstrip().split(".")[1])

sorted_extention_list = sorted(list(set(file_list)))
count_extention = Counter(file_list)

for extetison in sorted_extention_list:
    print(extetison, count_extention[extetison])