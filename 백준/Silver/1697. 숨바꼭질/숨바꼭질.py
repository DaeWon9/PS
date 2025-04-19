import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
max_range = 100000
INF = 2147483647

times = [INF] * (max_range + 1)
times[N] = 0

queue = deque([N])

while queue:
    v = queue.popleft()

    for nv in (v - 1, v + 1, 2 * v):
        if 0 <= nv <= max_range and times[nv] > times[v] + 1:
            times[nv] = times[v] + 1
            queue.append(nv)

print(times[K])
