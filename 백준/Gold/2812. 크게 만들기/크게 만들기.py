import sys

n, k = map(int, sys.stdin.readline().split())
numbers = list(sys.stdin.readline().rstrip())
stack = []

for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))