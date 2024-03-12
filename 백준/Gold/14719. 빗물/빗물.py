import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
block_info = list(map(int, input().split()))
queue = deque()
calc_queue = deque()

sum = 0

for block in block_info:
    if (not queue):
        queue.append(block)
        continue

    if (queue[0] <= block):
        pivot_block = queue[0]
        while queue:
            sum += pivot_block - queue.popleft()
        queue.append(block)
    else:
        queue.append(block)

if queue:
    queue.popleft()
    
while queue:
    block = queue.popleft()
        
    if (not calc_queue):
        calc_queue.append(block)
        continue

    if (calc_queue[-1] >= block or (queue and (block < max(queue)))):
        calc_queue.append(block)
        continue

    while calc_queue:
        target = calc_queue.popleft()
        if (target >= block):
            continue
        sum += block - target

print(sum)