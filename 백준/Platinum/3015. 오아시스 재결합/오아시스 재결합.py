import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = 0

for _ in range(N):
    h = int(input())

    while (stack and stack[-1][0] < h):
        hh, cc = stack.pop()
        answer += cc

    if (not stack):
        stack.append((h, 1))
        continue

    if (stack[-1][0] == h):
        hh, cc = stack.pop()
        answer += cc
        
        if (stack):
            answer += 1
        
        stack.append((h, cc+1))
    else: # 작음
        stack.append((h, 1))
        answer += 1

print(answer)