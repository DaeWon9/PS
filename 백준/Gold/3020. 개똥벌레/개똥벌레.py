import sys
from bisect import bisect_right
input = sys.stdin.readline

N, H = map(int, input().split())
bottom = [0] * H
top = [0] * H
result = [0] * H

for i in range(N):
    data = int(input())

    if (i % 2 == 0): # 아래
        bottom[data-1] += 1
    else:
        top[data-1] += 1

for i in range(H-2, -1, -1):
    bottom[i] += bottom[i+1]
    top[i] += top[i+1]

for i in range(H):
    result[i] = bottom[i] + top[H-i-1]

result.sort()
print(result[0], bisect_right(result, result[0]))