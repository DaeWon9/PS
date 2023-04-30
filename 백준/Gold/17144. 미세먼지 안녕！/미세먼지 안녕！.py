import sys
import math
from collections import deque

R, C, T = map(int, sys.stdin.readline().split())
direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]
top_air_cleaner_pos = []
bottom_air_cleaner_pos = []
room = []

def diffuse():
    dust_queue = deque()

    for row in range(R):
        for col in range(C):
            if (room[row][col] > 0):
                dust_queue.append((row, col, room[row][col]))
    
    while dust_queue:
        y, x, value = dust_queue.pop()
        dust_value = value
        diffused_dust_value = math.floor(dust_value / 5)
        count = 0

        for i in range(4):
            dx = x + direction_x[i]
            dy = y + direction_y[i]
            if (0 <= dx < C and 0 <= dy < R) and ([dy, dx] not in (top_air_cleaner_pos + bottom_air_cleaner_pos)):
                room[dy][dx] += diffused_dust_value
                count += 1
                
        room[y][x] -= (diffused_dust_value * count)

def first_purifier():
    for i in range(top_air_cleaner_pos[0][0]): # 좌
        if (room[top_air_cleaner_pos[0][0]-i][0] != -1):
            room[top_air_cleaner_pos[0][0]-i][0] = room[top_air_cleaner_pos[0][0]-1-i][0]
        else:
            room[top_air_cleaner_pos[0][0]-1-i][0] = 0

    for i in range(C-1): # 상
        room[0][i] = room[0][i+1]

    for i in range(top_air_cleaner_pos[0][0]): # 우
        room[i][C-1] = room[i+1][C-1]

    for i in range(C-1): # 하
        if (room[top_air_cleaner_pos[0][0]][C-2-i] != -1):
            room[top_air_cleaner_pos[0][0]][C-1-i] = room[top_air_cleaner_pos[0][0]][C-2-i]
        else:
            room[top_air_cleaner_pos[0][0]][C-1-i] = 0

def second_purifier():
    for i in range(R - bottom_air_cleaner_pos[0][0] - 1): # 좌
        if (room[bottom_air_cleaner_pos[0][0]+i][0] != -1):
            room[bottom_air_cleaner_pos[0][0]+i][0] = room[bottom_air_cleaner_pos[0][0]+1+i][0]
        else:
            room[bottom_air_cleaner_pos[0][0]+1+i][0] = 0

    for i in range(C-1): # 하
        room[R-1][i] = room[R-1][i+1]

    for i in range(R - bottom_air_cleaner_pos[0][0] - 1): # 우
        room[R-1-i][C-1] = room[R-2-i][C-1]

    for i in range(C-1): # 상
        if(room[bottom_air_cleaner_pos[0][0]][C-2-i] != -1):
            room[bottom_air_cleaner_pos[0][0]][C-1-i] = room[bottom_air_cleaner_pos[0][0]][C-2-i]
        else:
            room[bottom_air_cleaner_pos[0][0]][C-1-i] = 0


for i in range(R):
    row_list = list(map(int, sys.stdin.readline().split()))
    if (row_list[0] == -1):
        if(len(top_air_cleaner_pos) == 0):
            top_air_cleaner_pos.append([i,0])
        else:
            bottom_air_cleaner_pos.append([i,0])

    room.append(row_list)


for _ in range(T):
    diffuse()
    first_purifier()
    second_purifier()

result = 0
for row in room:
    result += sum(row)
print(result + 2)
