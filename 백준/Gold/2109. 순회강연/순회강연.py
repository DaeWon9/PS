import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = []
arr = [0] * 10001

for _ in range(n):
    p, d = map(int, input().split())
    data.append((p, d))

data.sort(key = lambda x : (-x[0], -x[1]))
queue = deque(data)

while queue:
    p, d = queue.popleft()

    if (arr[d] == 0):
        arr[d] = p
        continue

    min_idx = 1
    min_p = 10001
    for i in range(d, 0, -1):
        if (min_p > arr[i]):
            min_p = arr[i]
            min_idx = i
        
        if (min_p == 0):
            break
    
    if (min_p > p):
        continue

    arr[min_idx] = p

print(sum(arr))