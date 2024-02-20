import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc, row_size, col_size):
    if (0 <= dr < row_size and 0 <= dc < col_size):
        return True
    return False

def get_building_gate_pos(border, visited, building, own_key):

    for r, c in border:
        if (visited[r][c]):
            continue

        if (building[r][c] == '.'):
            return [r, c, 0]
        elif (building[r][c] == '$'):
            return [r, c, 1]
        elif (str(building[r][c]).islower()):
            return [r, c, 2]
        elif (str(building[r][c]).lower() in own_key):
            return [r, c, 3]

    return [-1, -1]

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

test_case = int(input())

for _ in range(test_case):
    building = []
    border = []
    answer = 0

    row_size, col_size = map(int, input().split())

    for r in range(row_size):
        input_list = list(input().rstrip())

        if (r == 0 or r == row_size - 1):
            for c in range(col_size):
                if (input_list[c] != '*'):
                    border.append((r, c))
        else:
            if (input_list[0] != '*'):
                border.append((r, 0))
            if (input_list[col_size - 1] != '*'):
                border.append((r, col_size - 1))

        building.append(input_list) 
    
    own_key = set(input().rstrip())
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]

    while True:
        gate_pos = get_building_gate_pos(border, visited, building, own_key)
        
        if (gate_pos[0] == -1):
            break

        queue = deque()
        queue.append((gate_pos[0], gate_pos[1]))

        if (gate_pos[2] == 1): # doc
            building[gate_pos[0]][gate_pos[1]] = '.'
            answer += 1
        if (gate_pos[2] == 2): # key
            own_key.add(building[gate_pos[0]][gate_pos[1]])
            building[gate_pos[0]][gate_pos[1]] = '.'
        elif (gate_pos[2] == 3): # door
            building[gate_pos[0]][gate_pos[1]] = '.'
        
        visited[gate_pos[0]][gate_pos[1]] = True

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                dr = r + direction_y[i]
                dc = c + direction_x[i]

                if (is_movable(dr, dc, row_size, col_size)):
                    current_area = str(building[dr][dc])

                    if (current_area == '*'):
                        continue

                    if (current_area == '$'):
                        answer += 1
                        building[dr][dc] = '.'
                        queue.append((dr, dc))
                        visited[dr][dc] = True
                        continue

                    if (current_area == '.' and not visited[dr][dc]):
                        queue.append((dr, dc))
                        visited[dr][dc] = True
                        continue

                    if (current_area.islower()): # key
                        prev_key_len = len(own_key)
                        own_key.add(current_area)
                        building[dr][dc] = '.'
                        queue.append((dr, dc))
                        
                        if (prev_key_len != len(own_key)):
                            queue.clear()
                            visited = [[False for _ in range(col_size)] for _ in range(row_size)]
                            visited[dr][dc] = True

                            queue.append((dr, dc))
                            break

                    if (current_area.isupper()): # door
                        if (current_area.lower() in own_key):
                            building[dr][dc] = '.'
                            queue.append((dr, dc))
                            visited[dr][dc] = True
                        continue
    print(answer)