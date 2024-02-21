import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
answer = 0

input_data = input().rstrip()
last_ch = ''

for ch in input_data:
    if (ch == '('):
        queue.append('(')
    else:
        queue.pop()
        if (last_ch == '('):
            answer += len(queue)
        else:
            answer += 1
    last_ch = ch

print(answer)