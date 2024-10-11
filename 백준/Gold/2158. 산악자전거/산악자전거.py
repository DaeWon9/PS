import sys
from collections import deque
input = sys.stdin.readline

# A -> B 이동 후 속도는 -> 기존 속도 * 2^(A-B) 

def is_movable(dr, dc):
    return (0 <= dr < R and 0 <= dc < C)

def calc_updated_speed(speed, A, B):
    return speed * pow(2, A - B)

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]

V, R, C = map(int, input().split()) # V 초기속도 / (R, C) 목적지
graph = []
queue = deque([(V, 0, 0, 0)])
time = [[2147483647 for _ in range(C)] for _ in range(R)]
time[0][0] = 0

for _ in range(R):
    graph.append(list(map(int, input().split())))

while queue:
    v, t, row, col = queue.popleft()

    if (time[row][col] < t):
        continue

    for i in range(4):
        dr = row + direction_y[i]
        dc = col + direction_x[i]

        if (is_movable(dr, dc)):
            move_time = 1 / v
            updated_time = t + move_time

            if (time[dr][dc] > updated_time):
                time[dr][dc] = updated_time
                updated_v = calc_updated_speed(v, graph[row][col], graph[dr][dc])
                queue.append((updated_v, updated_time, dr, dc))

print(f"{time[-1][-1]:.2f}")