import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

queue = deque()
answer = 0

for num in num_list: 
    if (not queue):
        queue.append(num)
    elif (queue[-1] < num):
        queue.append(num)
    else:
        queue.clear()
        queue.append(num)
    
    answer += len(queue)

print(answer)