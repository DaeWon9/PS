import sys
from collections import deque

current_pos, target_pos= map(int, sys.stdin.readline().rstrip().split())

map_list = [2147483647] * 100001
map_list[current_pos] = 0

queue = deque()
queue.append(current_pos)

while queue:
    pos = queue.popleft()

    if map_list[target_pos] > map_list[pos] + abs(target_pos - pos):
        map_list[target_pos] = map_list[pos] + abs(target_pos - pos)

    if pos - 1 >= 0 and map_list[pos - 1] > map_list[pos] + 1:
        map_list[pos - 1] = map_list[pos] + 1
        queue.append(pos - 1)
    
    if pos + 1 < 100001 and map_list[pos + 1] > map_list[pos] + 1:
        map_list[pos + 1] = map_list[pos] + 1
        queue.append(pos + 1)

    if pos * 2 < 100001 and map_list[pos * 2] > map_list[pos]:
        map_list[pos * 2] = map_list[pos]
        queue.append(pos * 2)
        
print(map_list[target_pos])