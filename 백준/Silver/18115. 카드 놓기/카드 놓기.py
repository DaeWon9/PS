import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
queue = deque()

for i in range(N-1, -1, -1):
    if (A[i] == 1):
        queue.appendleft(N-i)
    elif (A[i] == 2):
        tmp = queue.popleft()
        queue.appendleft(N-i)
        queue.appendleft(tmp)
    else: # 3
        queue.append(N-i)

print(*queue)