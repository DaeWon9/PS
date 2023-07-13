import sys

N = int(sys.stdin.readline())
A = set(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())

input_value = list(map(int, sys.stdin.readline().split()))

for value in input_value:
    if (value in A):
        print(1)
    else:
        print(0)
