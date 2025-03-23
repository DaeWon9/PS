import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
info_dict = defaultdict(int)

for _ in range(N):
    info_dict[int(input())] += 1

max_time = max(info_dict)
left = 1
right = M * max_time
answer = right

while (left <= right):
    mid = (left + right) // 2
    count = 0

    for key in info_dict:
        count += (mid // key) * info_dict[key]
        if (count >= M):
            break

    if (count >= M):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)