import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
result_list = [0 for _ in range(n)]
input_data = list(input().rstrip())

for id, data in enumerate(input_data):
    if (not queue):
        queue.append((data, id))
        continue
    
    if (data == ')'):
        pop_data, pop_id = queue.pop()
        if (pop_data == '('):
            result_list[id] = 1
            result_list[pop_id] = 1
    else:
        queue.append((data, id))

max_len = 0
temp_len = 0

for data in result_list:
    if (data == 1):
        temp_len += 1
    else:
        if (max_len < temp_len):
            max_len = temp_len
        temp_len = 0

if (max_len < temp_len):
    max_len = temp_len
    
print(max_len)