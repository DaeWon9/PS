from collections import deque
import sys

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
dq = deque()
 
for i in range(N):
    while dq and dq[-1][1] > A[i]:
        dq.pop()
    
    dq.append((i, A[i]))
 
    while dq and dq[0][0] < i - L + 1:
        dq.popleft()
        
    print(dq[0][1], end=" ")