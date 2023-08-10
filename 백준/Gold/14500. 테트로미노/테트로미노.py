import sys

block = [
    # ㅁ
    [(1, 0), (0, 1), (1, 1)],
    # ㅡ
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (0, 2), (0, 3)],
    # ㅗ
    [(1, 0), (1, 1), (2, 0)],
    [(1, 0), (1, -1), (2, 0)],
    [(0, 1), (1, 1), (0, 2)],
    [(0, 1), (-1, 1), (0, 2)],
    # ㄹ
    [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (-1, 1), (-1, 2)],
    [(1, 0), (1, -1), (2, -1)],
    [(1, 0), (1, 1), (2, 1)],
    # ㄴ
    [(0, 1), (0, 2), (1, 2)],
    [(0, 1), (0, 2), (-1, 2)],
    [(0, 1), (1, 0), (2, 0)],
    [(1, 0), (2, 0), (2, 1)],
    [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (0, 1), (0, 2)],
    [(0, 1), (-1, 1), (-2, 1)],
    [(0, 1), (1, 1), (2, 1)],
]


row_size, col_size = map(int, sys.stdin.readline().split())

board = []

for row in range(row_size):
    board.append(list(map(int, sys.stdin.readline().split())))

max_value = -1

for row in range(row_size):
    for col in range(col_size):
        for type in range(19):
            count = 0
            value = board[row][col]
            for index in range(3):
                dc = col + block[type][index][0]
                dr = row + block[type][index][1]

                if 0 <= dr < row_size and 0 <= dc < col_size:
                    value += board[dr][dc]
                    count += 1

            if count == 3:
                max_value = max(max_value, value)

print(max_value)