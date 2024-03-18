import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
max_len = 0
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

result = str(result_list).replace('[', '').replace(']', '').replace(', ','').split('0')

for d in result:
    temp_len = len(str(d))
    if (max_len < temp_len):
        max_len = temp_len

print(max_len)