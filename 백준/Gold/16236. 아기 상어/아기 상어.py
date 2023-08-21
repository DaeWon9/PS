import sys
from collections import deque


def find_the_nearest_eatable_fish():
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[baby_shark[0]][baby_shark[1]] = True  # current baby shark pos

    eatable_fish_list = []
    min_distance = -1

    queue = deque()
    queue.append((baby_shark[0], baby_shark[1], 0))

    while queue:
        row, col, distance = queue.popleft()

        if 0 < min_distance < distance:
            break

        if distance > 0 and 0 < board[row][col] < baby_shark[2]:  # the nearest eatable
            if min_distance == -1:
                min_distance = distance
            eatable_fish_list.append((distance, row, col))
        else:
            for index in range(4):
                dr = row + direction_y[index]
                dc = col + direction_x[index]

                if (
                    0 <= dr < N
                    and 0 <= dc < N
                    and not visited[dr][dc]
                    and board[dr][dc] <= baby_shark[2]
                ):
                    visited[dr][dc] = True
                    queue.append((dr, dc, distance + 1))

    if eatable_fish_list:
        eatable_fish_list.sort()
        row = eatable_fish_list[0][1]
        col = eatable_fish_list[0][2]

        board[row][col] = 0
        baby_shark[0] = row
        baby_shark[1] = col
        baby_shark[3] += 1

        if baby_shark[2] == baby_shark[3]:
            baby_shark[2] += 1
            baby_shark[3] = 0

        return eatable_fish_list[0][0]
    else:
        return -1


direction_x = [0, -1, 1, 0]  # 상 좌 우 하
direction_y = [-1, 0, 0, 1]

N = int(sys.stdin.readline())

baby_shark = []  # row, col, size, stack
board = []
time = 0

is_find_baby_shark = False

for row in range(N):
    input_list = list(map(int, sys.stdin.readline().split()))
    if not is_find_baby_shark:
        for col in range(N):
            if input_list[col] == 9:
                is_find_baby_shark = True
                baby_shark = [row, col, 2, 0]
                input_list[col] = 0

    board.append(input_list)

while True:
    distance = find_the_nearest_eatable_fish()
    if distance == -1:
        break

    time += distance

print(time)
