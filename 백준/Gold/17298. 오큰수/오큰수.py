import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
stack = []
R_NGE = []

while arr:
    target = arr.pop()
    if (not stack):
        R_NGE.append(-1)
    else:
        while (stack and stack[-1] <= target):
            stack.pop()

        if (stack):
            R_NGE.append(stack[-1])
        else:
            R_NGE.append(-1)

    stack.append(target)

print(*reversed(R_NGE))