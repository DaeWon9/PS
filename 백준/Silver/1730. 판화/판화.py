import sys
input = sys.stdin.readline

def is_movable(r, c):
    return (0 <= r < N and 0 <= c < N)

def move(row, col, dr, dc, mark):
    new_row, new_col = row + dr, col + dc
    if is_movable(new_row, new_col):
        board_status[row][col] |= mark
        board_status[new_row][new_col] |= mark
        return new_row, new_col
    return row, col

N = int(input())
input_datas = input().rstrip()
board_status = [[0 for _ in range(N)] for _ in range(N)]
row, col = 0, 0

directions = {
    'U': (-1, 0, 1),  # Up
    'D': (1, 0, 1),   # Down
    'R': (0, 1, 2),   # Right
    'L': (0, -1, 2)   # Left
}

for data in input_datas:
    if data in directions:
        dr, dc, mark = directions[data]
        row, col = move(row, col, dr, dc, mark)

for row_status in board_status:
    for status in row_status:
        if status == 0:
            print('.', end='')
        elif status == 1:
            print('|', end='')
        elif status == 2:
            print('-', end='')
        else:
            print('+', end='')
    print()
