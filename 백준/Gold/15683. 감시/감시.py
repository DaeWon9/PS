import sys
from itertools import product
import copy
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < n and 0 <= dc < m):
        return True
    return False

direction_x = [0, 0, -1, 1]
direction_y = [-1, 1, 0, 0]

cctv_direction_dict = {
    1 : [0, 1, 2, 3], 
    2 : [(0, 1), (2, 3)],
    3 : [(0, 3), (1, 3), (1, 2), (0, 2)],
    4 : [(0, 2, 3), (0, 1, 3), (1, 2, 3), (0, 1, 2)],
    5 : [(0, 1, 2, 3)],
}

n, m = map(int, input().split())
board = []

cctv_list = []
cctv_direction_list = []

answer = 2147483647

for r in range(n):
    input_data = list(map(int, input().split()))

    for c in range(m):
        if (input_data[c] != 0 and input_data[c] != 6):
            cctv_list.append((input_data[c], r, c)) # type, row, col
            cctv_direction_list.append(cctv_direction_dict[input_data[c]])

    board.append(input_data)

for case in list(product(*cctv_direction_list)):
    copied_board = copy.deepcopy(board)

    for id, direction in enumerate(case):
        cctv_row = cctv_list[id][1]
        cctv_col = cctv_list[id][2]
        
        if (type(direction) == tuple):
            for dir in direction:
                dr = cctv_row
                dc = cctv_col
                while True:
                    dr += direction_y[dir]
                    dc += direction_x[dir]

                    if (is_movable(dr, dc) and copied_board[dr][dc] != 6):
                        copied_board[dr][dc] = 9
                    else:
                        break
        else:
            while True:
                dr = cctv_row + direction_y[direction]
                dc = cctv_col + direction_x[direction]

                if (is_movable(dr, dc) and copied_board[dr][dc] != 6):
                    copied_board[dr][dc] = 9
                    cctv_row = dr
                    cctv_col = dc
                else:
                    break

    count = 0
    for r in copied_board:
        count += r.count(0)
    
    if (answer > count):
        answer = count

print(answer)