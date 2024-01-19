import sys
from collections import deque

def L():
    if not prev_string:
        return
    target_char = prev_string.pop()
    next_string.appendleft(target_char)

def D():
    if not next_string:
        return
    target_char = next_string.popleft()
    prev_string.append(target_char)

def B():
    if not prev_string:
        return
    prev_string.pop()

def P(ch):
    prev_string.append(ch)

prev_string = deque(sys.stdin.readline().rsplit()[0])
next_string = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    process = sys.stdin.readline().rstrip().split()
    if (process[0] == 'L'):
        L()
    elif (process[0] == 'D'):
        D()
    elif (process[0] == 'B'):
        B()
    else:
        P(process[1])

answer = prev_string + next_string
while answer:
    print(answer.popleft(), end = '')