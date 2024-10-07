import sys
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().split())
power_list = []
seleted_list = []

for row in range(N):
    sorted_list = sorted(list(map(int, input().split())))
    power_list.append(sorted_list)

    seleted_list.append((sorted_list[0], row, 0)) # (value, row, col)

seleted_list.sort()
seleted_list = deque(seleted_list)
diff = seleted_list[-1][0] - seleted_list[0][0]

for i in range(N * M):
    min_value, current_row, current_col = seleted_list.popleft()

    if (current_col == M - 1):
        break

    next_col = current_col + 1
    next_value = power_list[current_row][next_col]

    target_index = bisect_left(seleted_list, (next_value, current_row, next_col))
    seleted_list.insert(target_index, (next_value, current_row, next_col))

    new_diff = seleted_list[-1][0] - seleted_list[0][0]

    if (new_diff < diff):
        diff = new_diff

print(diff)