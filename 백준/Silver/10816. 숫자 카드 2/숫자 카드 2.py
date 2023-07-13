import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

input_value = list(map(int, sys.stdin.readline().split()))

counter = Counter(A)

for value in input_value:
    print(counter[value])
