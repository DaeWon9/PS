import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def is_movable(v):
    return (0 <= v < 100001)

def find_path(v, path: list):
    if (path[-1] == N):
        print(*path[::-1])
        exit(0)

    nv = v - 1
    if (is_movable(nv) and time[nv] + 1 == time[v]):
        path.append(nv)
        find_path(nv, path)
        path.pop()

    nv = v + 1
    if (is_movable(nv) and time[nv] + 1 == time[v]):
        path.append(nv)
        find_path(nv, path)
        path.pop()

    if (v % 2 == 0):
        nv = v // 2
        if (is_movable(nv) and time[nv] + 1 == time[v]):
            path.append(nv)
            find_path(nv, path)
            path.pop()


N, K = map(int, input().split())
queue = deque()

time = [float('inf') for _ in range(100001)]
time[N] = 0

queue.append((N, 0))

while queue:
    v, t = queue.popleft() 

    if (v == K):
        print(t)
        break

    nv = v + 1
    if (is_movable(nv)):
        if (time[nv] > t + 1):
            time[nv] = t + 1
            queue.append((nv, t+1))
    
    nv = v - 1
    if (is_movable(nv)):
        if (time[nv] > t + 1):
            time[nv] = t + 1
            queue.append((nv, t+1))

    nv = v * 2
    if (is_movable(nv)):
        if (time[nv] > t + 1):
            time[nv] = t + 1
            queue.append((nv, t+1))

find_path(K, [K])