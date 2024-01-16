import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
computer_dict = defaultdict(list)
connected_count_list = []

def get_connected_computer_count(root_computer):
    visited = [False for _ in range(n + 1)]
    queue = deque()
    queue.append(root_computer)

    count = 0

    while queue:
        temp_computer = queue.popleft()

        for computer in computer_dict[temp_computer]:
            if (not visited[computer]):
                visited[computer] = True
                queue.append(computer)
                count += 1
                
        visited[temp_computer] = True

    return count

for _ in range(m):
    a_computer, b_computer = map(int, sys.stdin.readline().split()) # a 가 b 를 신뢰
    computer_dict[b_computer].append(a_computer)

for key in range(1, n + 1):
    connected_count_list.append((key, get_connected_computer_count(key)))

connected_count_list.sort(key = lambda x : (-x[1], x[0]))
max_count = connected_count_list[0][1]

for count_info in connected_count_list:
    if (count_info[1] != max_count):
        break

    print(count_info[0], end=' ')