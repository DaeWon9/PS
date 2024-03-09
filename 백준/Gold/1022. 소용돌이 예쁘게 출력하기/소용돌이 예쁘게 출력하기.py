import sys
input = sys.stdin.readline

def is_in_board(dr, dc):
    if (0 <= dr < row_size and 0 <= dc < col_size):
        return True
    return False

direction_x = [1, 0, -1, 0] # 우 상 좌 하
direction_y = [0, -1, 0, 1]

r1, c1, r2, c2 = map(int, input().split())

row_size = r2 - r1 + 1
col_size = c2 - c1 + 1

start_row = 0 - r1
start_col = 0 - c1

board = [[0 for _ in range(col_size)] for _ in range(row_size)]
max_fill_count = row_size * col_size
direction = 0
direction_change_count = 0
value = 1
length = 1
fill_count = 1

if (is_in_board(start_row, start_col)):
    board[start_row][start_col] = 1
else:
    fill_count = 0

while fill_count < max_fill_count:
    dr = start_row
    dc = start_col

    for c in range(length):
        dr += direction_y[direction]
        dc += direction_x[direction]

        value += 1
        if (is_in_board(dr, dc)):
            board[dr][dc] = value
            fill_count += 1

    start_row = dr
    start_col = dc

    direction_change_count += 1 
    direction = (direction + 1) % 4

    if (direction_change_count % 2 == 0):
        length += 1

last_value = 0
for row in board:
    last_value = max(last_value, max(row))
    
format_number = len(str(last_value))

for row in board:
    for number in row:
        print("%*d" %(format_number, number), end = ' ')
    print()