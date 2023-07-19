import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
i = 0
result = deque()

for _ in range(n):
    x = int(sys.stdin.readline())
    while i < x:
        i += 1
        stack.append(i)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit()

print('\n'.join(result))
