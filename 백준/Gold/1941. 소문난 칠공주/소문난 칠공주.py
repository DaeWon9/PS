import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]

def is_movable(dr, dc):
    return (0 <= dr < 5 and 0 <= dc < 5)

def is_linked(pos_set):
    board = [[0 for _ in range(5)] for _ in range(5)]
    visited = [[False for _ in range(5)] for _ in range(5)]
    visit_count = 0
    
    for r, c in pos_set:
        board[r][c] = 1

    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for idx in range(4):
            dr = r + direction_y[idx]
            dc = c + direction_x[idx]

            if (is_movable(dr, dc) and not visited[dr][dc] and board[dr][dc] == 1):
                queue.append((dr, dc))
                visited[dr][dc] = True
                visit_count += 1

    if (visit_count == 6):
        return 1
    return 0
    
s_type_pos_set = set()
y_type_pos_set = set()
answer = 0

for row in range(5):
    input_data = list(input().rstrip())

    for col, type in enumerate(input_data):
        if (type == 'S'):
            s_type_pos_set.add((row, col))
        else:
            y_type_pos_set.add((row, col))

whole_type_pos_set = s_type_pos_set.union(y_type_pos_set)

for combi in list(combinations(whole_type_pos_set, 7)):
    if (len(set(combi).intersection(s_type_pos_set)) < 4):
        continue
    
    answer += is_linked(combi)

print(answer)