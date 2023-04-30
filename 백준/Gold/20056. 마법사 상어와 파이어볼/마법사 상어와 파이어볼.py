import sys
from collections import deque
import math

direction_x = [0, 1, 1, 1, 0, -1, -1, -1]
direction_y = [-1, -1, 0, 1, 1, 1, 0, -1]
fire_ball_list = [] # 0:r, 1:c, 2:m, 3:s, 4:d

N, M, K = map(int, sys.stdin.readline().split())

def move_fire_ball():
    fire_ball_map = [[0] * N for _ in range(N)]
    for fire_ball in fire_ball_list:
        y = fire_ball[0]
        x = fire_ball[1]

        dx = x + (direction_x[fire_ball[4]] * (fire_ball[3] % N))
        dy = y + (direction_y[fire_ball[4]] * (fire_ball[3] % N))

        if (dx > N-1): 
            dx = dx - N
        elif (dx < 0):
            dx = N + dx

        if (dy > N-1):
            dy = dy - N
        elif (dy < 0):
            dy = N + dy

        fire_ball[0] = dy
        fire_ball[1] = dx
        fire_ball_map[dy][dx] += 1
    return fire_ball_map

def find_duplicated_fire_ball():
    fire_ball_queue = deque()

    for row in range(N):
        for col in range(N):
            if (fire_ball_map[row][col] > 1):
                fire_ball_queue.append((row, col, fire_ball_map[row][col]))

    while fire_ball_queue:
        direction_style = [False, False]
        m_sum = 0
        s_sum = 0
        row, col, count = fire_ball_queue.pop()
        delete_list = []
        
        for i in range(len(fire_ball_list)):
            if (fire_ball_list[i][0] == row and fire_ball_list[i][1] == col):
                m_sum += fire_ball_list[i][2]
                s_sum += fire_ball_list[i][3]
                if (fire_ball_list[i][4] % 2 == 0):
                    direction_style[0] = True
                else:
                    direction_style[1] = True
        
                delete_list.append(i)

        cnt =  0
        for i in delete_list:
            del fire_ball_list[i - cnt]
            cnt += 1
        
        new_m = math.floor(m_sum / 5)
        new_s = math.floor(s_sum / count)
        d_list = [0, 2, 4, 6]
        if (direction_style[0] == direction_style[1]):
            d_list = [1, 3, 5, 7]
        
        if (new_m > 0):
            for i in range(4):
                fire_ball_list.append([row, col, new_m, new_s, d_list[i]])

for _ in range(M): 
    input_list = list(map(int, sys.stdin.readline().rsplit()))
    input_list[0] -= 1
    input_list[1] -= 1
    fire_ball_list.append(input_list)

for i in range(K):
    fire_ball_map = move_fire_ball()
    find_duplicated_fire_ball()

result = 0
for fire_ball in fire_ball_list:
    result += fire_ball[2]
print(result)