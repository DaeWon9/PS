import sys
from collections import deque

direction_x = [1, -1, 0, 0, 0, 0]
direction_y = [0, 0, 1, -1, 0, 0]
direction_z = [0, 0, 0, 0, 1, -1]

def ripe_tomato():
    unripe_tomato_count = 0
    day = 0
    ripe_tomato_queue = deque()

    for h in range(height_size):
        for row in range(row_size):
            for col in range(col_size):
                if tomato_box[h][row][col] == 1:
                    ripe_tomato_queue.append((h, row, col))
                elif tomato_box[h][row][col] == 0:
                    unripe_tomato_count += 1

    while ripe_tomato_queue:
        h, r, c = ripe_tomato_queue.pop()
        for index in range(6):
            dh = h + direction_z[index]
            dr = r + direction_y[index]
            dc = c + direction_x[index]

            if (
                0 <= dh < height_size
                and 0 <= dr < row_size
                and 0 <= dc < col_size
                and tomato_box[dh][dr][dc] == 0
            ):
                tomato_box[dh][dr][dc] = tomato_box[h][r][c] + 1
                day = max(day, tomato_box[dh][dr][dc])
                ripe_tomato_queue.appendleft((dh, dr, dc))
                unripe_tomato_count -= 1

    return unripe_tomato_count, day

col_size, row_size, height_size = map(int, sys.stdin.readline().rstrip().split())

tomato_box = [
    [[0 for _ in range(col_size)] for _ in range(row_size)] for _ in range(height_size)
]

for h in range(height_size):
    for row in range(row_size):
        tomato_box[h][row] = list(map(int, sys.stdin.readline().rstrip().split()))

unripe_tomato_count, day = ripe_tomato()

if unripe_tomato_count == 0:
    if day != 0:
        day -= 1
    print(day)
else:
    print("-1")