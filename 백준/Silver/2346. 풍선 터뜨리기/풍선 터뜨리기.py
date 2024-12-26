import sys
from collections import deque
input = sys.stdin.readline

N  = int(input()) # 0은 없다
dq = deque(enumerate(map(int, input().split())))

while dq:
    idx, now_turn = dq.popleft()
    print(idx + 1, end=' ')

    if (now_turn > 0):
        dq.rotate(-(now_turn - 1))
    else:
        dq.rotate(-now_turn)