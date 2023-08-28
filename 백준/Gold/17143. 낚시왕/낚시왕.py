import sys
from collections import defaultdict

row_size, col_size, shark_count = map(int, sys.stdin.readline().split())

sharks = []  # id, row, col, 속력, 방향, 크기
died_shark_id_list = set()
fisher_king_col = -1
answer = 0
direction_x = [0, 0, 0, 1, -1]  # 상 하 우 좌
direction_y = [0, -1, 1, 0, 0]


def change_direction(current_direction):
    if current_direction == 1:
        return 2
    elif current_direction == 2:
        return 1
    elif current_direction == 3:
        return 4
    else:
        return 3


def move_shark():
    shark_pos_dict = defaultdict(set)
    for shark_id in range(shark_count):
        if shark_id in died_shark_id_list:  # can't move
            continue

        is_completed = False
        move_count = 0

        if sharks[shark_id][3] == 0:  # speed zero
            is_completed = True

        while not is_completed:
            dr = sharks[shark_id][1] + direction_y[sharks[shark_id][4]]
            dc = sharks[shark_id][2] + direction_x[sharks[shark_id][4]]
            if 0 <= dr < row_size and 0 <= dc < col_size:  # can move
                sharks[shark_id][1] = dr
                sharks[shark_id][2] = dc
                move_count += 1
            else:  # can't move
                sharks[shark_id][4] = change_direction(sharks[shark_id][4])

            if move_count >= sharks[shark_id][3]:
                is_completed = True

        shark_pos_dict[(sharks[shark_id][1], sharks[shark_id][2])].add(shark_id)

    for overlaped_sharks in shark_pos_dict.values():
        if len(overlaped_sharks) < 2:
            continue

        max_size_shark = [-1, -1]  # id, size

        for shark_id in overlaped_sharks:
            if sharks[shark_id][5] > max_size_shark[1]:
                if max_size_shark[0] != -1:
                    died_shark_id_list.add(max_size_shark[0])
                max_size_shark = [shark_id, sharks[shark_id][5]]
            else:
                died_shark_id_list.add(shark_id)


def catch_shark():
    global answer
    catchable_shark_id_list = []
    for shark in sharks:
        id = shark[0]
        row = shark[1]
        col = shark[2]
        if fisher_king_col == col and id not in died_shark_id_list:
            catchable_shark_id_list.append((row, id))

    if catchable_shark_id_list:
        catchable_shark_id_list.sort()
        died_shark_id_list.add(catchable_shark_id_list[0][1])
        answer += sharks[catchable_shark_id_list[0][1]][5]


for shark_id in range(shark_count):
    shark = list(map(int, sys.stdin.readline().split()))
    shark.insert(0, shark_id)
    shark[1] -= 1
    shark[2] -= 1
    if shark[4] <= 2:  # 상 or 하
        shark[3] %= (row_size - 1) * 2
    else:  # 좌 or 우
        shark[3] %= (col_size - 1) * 2
    sharks.append(shark)

while fisher_king_col < col_size - 1:
    fisher_king_col += 1
    catch_shark()
    move_shark()

print(answer)
