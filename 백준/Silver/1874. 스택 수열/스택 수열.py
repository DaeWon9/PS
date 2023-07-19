import sys

n = int(sys.stdin.readline())
stack = []
i = 0
result = []

for _ in range(n):
    x = int(sys.stdin.readline())
    while True:
        if x in stack:
            if stack[-1] == x:
                stack.pop()
                result.append('-')
                break
            else:
                print("NO")
                sys.exit()
        else:
            if i+1 > x:
                print("NO")
                sys.exit()
            else:
                i += 1
                stack.append(i)
                result.append('+')

print('\n'.join(result))
