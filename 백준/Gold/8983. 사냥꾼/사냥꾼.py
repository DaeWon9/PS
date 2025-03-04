import sys
from bisect import bisect_left

input = sys.stdin.readline

M, N, L = map(int, input().split())
poses = list(map(int, input().split()))
poses.sort()

answer = 0

for _ in range(N):
    x, y = map(int, input().split())

    if (y > L):
        continue

    idx = bisect_left(poses, x)

    left_pivot_x = poses[idx - 1] if idx > 0 else float('-inf')
    right_pivot_x = poses[idx] if idx < M else float('inf')

    if (abs(left_pivot_x - x) + y <= L or abs(right_pivot_x - x) + y <= L):
        answer += 1

print(answer)
