import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N):
    document_count, target_index = map(int, sys.stdin.readline().split())
    document_priority_list = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    for i in range(document_count):
        queue.append((i, document_priority_list[i]))

    document_priority_list.sort(reverse=True)
    
    count = 1
    while(queue):
        value = queue.popleft()
        if (value[1] == document_priority_list[0]):
            if (value[0] == target_index):
                break
            count += 1
            document_priority_list.remove(document_priority_list[0])
        else:
            queue.append(value)

    print(count)

