import sys
from collections import deque
input = sys.stdin.readline

TOP = 0
LEFT = 6
RIGHT = 2

wheel_infos = []
for _ in range(4):
    wheel_infos.append(deque(map(str, input().rstrip())))

K = int(input())
for _ in range(K):
    action_queue = deque()

    # 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.
    target_idx, direction = map(int, input().split())
    target_idx -= 1

    action_queue.append((target_idx, direction))

    # check right side
    for i in range(target_idx, 3):
        if (wheel_infos[i][RIGHT] == wheel_infos[i+1][LEFT]):
            break
        
        if (target_idx % 2 == i % 2):
            action_queue.append((i+1, -direction))
        else:
            action_queue.append((i+1, direction))

    # check left side
    for i in range(target_idx, 0, -1):
        if (wheel_infos[i][LEFT] == wheel_infos[i-1][RIGHT]):
            break
        
        if (target_idx % 2 == i % 2):
            action_queue.append((i-1, -direction))
        else:
            action_queue.append((i-1, direction))
    
    while action_queue:
        idx, dir = action_queue.popleft()
        wheel_infos[idx].rotate(dir)

answer = 0
if (wheel_infos[0][TOP] == '1'):
    answer += 1
if (wheel_infos[1][TOP] == '1'):
    answer += 2
if (wheel_infos[2][TOP] == '1'):
    answer += 4
if (wheel_infos[3][TOP] == '1'):
    answer += 8

print(answer)