import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
circle_list = []
stack = deque()

for id in range(N):
    x, r = map(int, input().split())
    circle_list.append((x + r, id))
    circle_list.append((x - r, id))

circle_list.sort()

for distance, circle_id in circle_list:
    if stack:
        top_circle_id = stack[-1]
        if (top_circle_id == circle_id):
            stack.pop()
        else:
            stack.append(circle_id)
    else:
        stack.append(circle_id)

if stack:
    print('NO')
else:
    print('YES')