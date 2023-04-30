import sys

N, M = map(int, sys.stdin.readline().split())
basket_list = []
direction_x = [0, -1, -1, 0, 1, 1, 1, 0, -1]
direction_y = [0, 0, -1, -1, -1, 0, 1, 1, 1]
diagonal_x = [-1, 1, 1, -1]
diagonal_y = [1, 1, -1, -1]
cloud_pos = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

def rain(move_type, move_count, cloud_pos):
    moved_cloud_pos = []
    for pos_y, pos_x in cloud_pos: # 구름 이동 후 비내리기
        pos_x = pos_x + (direction_x[move_type] * (move_count % N))
        pos_y = pos_y + (direction_y[move_type] * (move_count % N))
        if (pos_x > N-1): 
            pos_x = pos_x - N
        elif (pos_x < 0):
            pos_x = N + pos_x

        if (pos_y > N-1):
            pos_y = pos_y - N
        elif (pos_y < 0):
            pos_y = N + pos_y

        basket_list[pos_y][pos_x] += 1
        moved_cloud_pos.append((pos_y, pos_x))

    for row, col in moved_cloud_pos: # 대각선 판단 후 물 증가
        water_existence_count = 0
        for i in range(4):
            dx = col + diagonal_x[i]
            dy = row + diagonal_y[i]
            if (0 <= dx < N and 0 <= dy < N):
                if (basket_list[dy][dx] > 0):
                    water_existence_count += 1
        basket_list[row][col] += water_existence_count

    return set_cloud(moved_cloud_pos)# 구름 새롭게 배치

def set_cloud(moved_cloud_pos):
    new_cloud_pos = []
    for row in range(N):
        for col in range(N):
            if (basket_list[row][col] >= 2) and ((row, col) not in moved_cloud_pos):
                basket_list[row][col] -= 2
                new_cloud_pos.append((row, col))
    return new_cloud_pos

for _ in range(N):
    basket_list.append(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    type, count = map(int, sys.stdin.readline().split())
    cloud_pos = rain(type, count, cloud_pos)

result = 0
for row in basket_list:
    result += sum(row)

print(result)