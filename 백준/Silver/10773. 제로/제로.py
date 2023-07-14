import sys
from collections import deque

K = int(sys.stdin.readline())

stack = deque()

for i in range(K):
    input_num = int(sys.stdin.readline())
    if(input_num != 0):
        stack.append(input_num)
    else:
        stack.pop()

print(sum(stack))