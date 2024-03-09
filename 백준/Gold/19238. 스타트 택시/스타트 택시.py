import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def get_nearest_passenger():
    queue = deque()
    visited = set()
    visited.add((texi_pos_row, texi_pos_col))
    queue.append((0, texi_pos_row, texi_pos_col))

    time_check = -1
    passenger_list = []

    while queue:
        time, row, col = queue.popleft()

        if ((row, col) in passenger_pos_set):
            if (time_check == -1):
                time_check = time
            
            if (time_check < time):
                break

            passenger_list.append((time, row, col))

        for i in range(4):
            dr = row + direction_y[i]
            dc = col + direction_x[i]

            if (is_movable(dr, dc) and (dr, dc) not in visited and board[dr][dc] == 0):
                queue.append((time + 1, dr, dc))
                visited.add((dr, dc))
    
    if (passenger_list):
        passenger_list.sort(key = lambda x : (x[1], x[2]))
        return passenger_list[0]
    
    return (-1, -1, -1)

def go_to_destination(start_pos_row, start_pos_col):
    destination_pos_row, destination_pos_col = passenger_destination_dict[(start_pos_row, start_pos_col)]

    queue = deque()
    visited = set()
    visited.add((start_pos_row, start_pos_col))
    queue.append((0, start_pos_row, start_pos_col))

    while queue:
        time, row, col = queue.popleft()

        if (row == destination_pos_row and col == destination_pos_col):
            return (time, row, col)

        for i in range(4):
            dr = row + direction_y[i]
            dc = col + direction_x[i]

            if (is_movable(dr, dc) and (dr, dc) not in visited and board[dr][dc] == 0):
                queue.append((time + 1, dr, dc))
                visited.add((dr, dc))
    
    return (-1, -1, -1)

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < N):
        return True
    return False

direction_x = [0, -1, 1, 0] # 상 좌 우 하 -> row 우선, col 우선
direction_y = [-1, 0, 0, 1]

N, M, gas = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

texi_pos_row, texi_pos_col = map(int, input().split())
texi_pos_row -= 1
texi_pos_col -= 1
passenger_pos_set = set()
passenger_destination_dict = defaultdict(tuple)

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    passenger_pos_set.add((r1 - 1, c1 - 1))
    passenger_destination_dict[(r1 - 1, c1 - 1)] = (r2 - 1,  c2 - 1)

for _ in range(M):
    time, row, col = get_nearest_passenger()
    if (time == -1 or time > gas):
        print(-1)
        exit(0)
    gas -= time
    passenger_pos_set.discard((row, col))

    time, row, col = go_to_destination(row, col)
    if (time == -1 or time > gas):
        print(-1)
        exit(0)
    
    gas -= time
    gas += (time * 2)

    texi_pos_row = row
    texi_pos_col = col

print(gas)