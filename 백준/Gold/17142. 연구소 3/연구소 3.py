import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < N):
        return True
    return False

N, M = map(int, input().split())
virus_pos = []
wall_pos = set()

for row in range(N):
    datas = list(map(int, input().split()))

    for col, data in enumerate(datas):
        if (data == 2): # virus
            virus_pos.append((row, col))
        elif (data == 1): # wall
            wall_pos.add((row, col))

area_count = N * N - len(virus_pos) - len(wall_pos)

if (area_count == 0):
    print(0)
    exit(0)
    
direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]
answer = 2147483647

for combi in list(combinations(virus_pos, M)):
    queue = deque((r, c, 0) for r, c in combi)  # init
    visited_area = set(combi)
    visit_count = 0

    while queue:
        row, col, time = queue.popleft()

        if (answer <= time):
            break

        for idx in range(4):
            dr = row + direction_y[idx]
            dc = col + direction_x[idx]

            if (is_movable(dr, dc) and (dr, dc) not in wall_pos and (dr, dc) not in visited_area):
                queue.append((dr, dc, time + 1))
                visited_area.add((dr, dc))

                if ((dr, dc) not in virus_pos):
                    visit_count += 1

        if (visit_count == area_count and answer > time + 1):
            answer = time + 1
            break
            
if (answer == 2147483647):
    print(-1)
else:
    print(answer)