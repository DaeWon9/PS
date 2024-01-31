import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
top_list = list(map(int, input().split()))
stack = deque()

for num in range(n):
    while stack and stack[-1][1] < top_list[num]:
        stack.pop()
    
    if not stack:
        print(0, end=' ')
        stack.append([num + 1, top_list[num]])
        continue

    print(stack[-1][0], end=' ')
    stack.append([num + 1, top_list[num]])