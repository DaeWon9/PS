import sys
import math
from collections import deque
input = sys.stdin.readline

# 연로통 사이즈를 이분탐색으로 정한다.
# 해당 사이즈의 연로통을 장착하고 비행을 해본다.
# k번 이하로 급유를 받는 횟수가 형성되면 answer을 업데이트하고 연료통 사이즈를 줄인다.
# 급유받는 횟수가 k번을 초과하면 연료통 사이즈를 늘린다.

def get_refueling_count(fuel_size):
    queue = deque()
    queue.append((0, 0, 0)) # cnt, r, c

    visited = [False] * (n+1)
    visited[0] = True

    while queue:
        cnt, r, c = queue.popleft()

        if (cnt > k):
            continue

        if (get_needed_fuel(r, c, 10000, 10000) <= fuel_size):
            return cnt
        
        for i in range(1, n+1):
            if (visited[i]):
                continue

            nr, nc = poses[i]
            
            needed_fuel = get_needed_fuel(r, c, nr, nc)

            if (needed_fuel > fuel_size):
                continue

            queue.append((cnt+1, nr, nc))
            visited[i] = True

    return 1416
    

def get_needed_fuel(r1, c1, r2, c2):
    distance = math.sqrt((r1-r2) ** 2 + (c1-c2) ** 2)
    fuel = distance // 10

    if (distance % 10 != 0):
        fuel += 1

    return fuel

n, k = map(int, input().split())
poses = [(0, 0)]

for _ in range(n):
    r, c = map(int, input().split())
    poses.append((r, c))

left = 0
right = 1415
answer = 0

while (left <= right):
    mid = (left + right) // 2

    refueling_count = get_refueling_count(mid)

    if (refueling_count <= k):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
