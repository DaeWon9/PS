import sys
from collections import deque, defaultdict
import copy

direction_x = [0, 0, -1, -1, -1, 0, 1, 1, 1]  # index 1 부터 ↑, ↖, ←, ↙, ↓, ↘, →, ↗
direction_y = [0, -1, -1, 0, 1, 1, 1, 0, -1]


def move_and_eat_fish(shark):
    global answer
    shark_row, shark_col, shark_direction, eaten_fish, board, fish = shark
    copy_fish = copy.deepcopy(fish)

    current_board = copy.deepcopy(board)

    for fish_id in range(1, 17):
        moved_completed = False

        row, col, direction = copy_fish[fish_id]
        if fish_id in eaten_fish:  # die
            # print(fish_id, "is died")
            continue

        while not moved_completed:
            dr = row + direction_y[direction]
            dc = col + direction_x[direction]

            if (
                (0 <= dr < 4) and (0 <= dc < 4) and (dr != shark_row or dc != shark_col)
            ):  # can move
                temp_fish = current_board[dr][dc]
                current_board[dr][dc] = fish_id
                current_board[row][col] = temp_fish

                copy_fish[temp_fish][0] = row
                copy_fish[temp_fish][1] = col

                copy_fish[fish_id][0] = dr
                copy_fish[fish_id][1] = dc

                copy_fish[fish_id][2] = direction
                moved_completed = True
            else:
                direction = direction + 1
                if direction > 8:
                    direction = direction % 8

    new_board = copy.deepcopy(current_board)

    for _ in range(3):  # shark max move 3
        dr = shark_row + direction_y[shark_direction]
        dc = shark_col + direction_x[shark_direction]

        if 0 <= dr < 4 and 0 <= dc < 4:  # can eat
            shark_row = dr
            shark_col = dc
            if new_board[dr][dc] not in eaten_fish:
                new_eaten_fish = copy.deepcopy(eaten_fish)
                new_eaten_fish.append(new_board[dr][dc])
                answer = max(answer, sum(new_eaten_fish))
                queue.append(
                    (
                        shark_row,
                        shark_col,
                        copy_fish[new_board[dr][dc]][2],
                        new_eaten_fish,
                        new_board,
                        copy_fish,
                    )
                )


fish = defaultdict(list)

board = [[0 for _ in range(4)] for _ in range(4)]

shark = [0, 0, 0, [], [], fish]
answer = 0

for row in range(4):
    input_string = list(map(int, sys.stdin.readline().split()))
    fish_id = 0
    for index in range(8):
        if index % 2 == 0:
            fish_id = input_string[index]
            board[row][index // 2] = input_string[index]

        else:
            fish[fish_id] = [row, index // 2, input_string[index]]

            if row == 0 and index == 1:
                shark[2] = input_string[index]  # set shark direction
                shark[3].append(fish_id)


shark[4] = board

queue = deque()
queue.append(shark)

while queue:
    shark = queue.popleft()
    move_and_eat_fish(shark)
print(answer)
