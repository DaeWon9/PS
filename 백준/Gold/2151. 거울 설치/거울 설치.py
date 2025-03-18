import sys
import heapq
input = sys.stdin.readline

DIRECTION_UP = 0
DIRECTION_RIGHT = 1
DIRECTION_DOWN = 2
DIRECTION_LEFT = 3

def is_movable(r, c):
    return (0 <= r < N and 0 <= c < N)

def rotate_right(dir):
    return (dir + 1) % 4

def rotate_left(dir):
    return (dir + 3) % 4

direction_x = [0, 1, 0, -1]
direction_y = [-1, 0, 1, 0]

N = int(input())
wall_pos_set = set()
mirror_pos_set = set()
door_pos_list = []

for r in range(N):
    input_data = input().rstrip()

    for c in range(N):
        data = input_data[c]

        if (data == '*'):
            wall_pos_set.add((r, c))
        elif (data == '#'):
            door_pos_list.append((r, c))
        elif (data == '!'):
            mirror_pos_set.add((r, c))

start_door, goal_door = door_pos_list
heap = []

for i in range(4):
    heapq.heappush(heap, (0, i, start_door[0], start_door[1]))

visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(4)]
visited[DIRECTION_UP][start_door[0]][start_door[1]] = True

while heap:
    m_cnt, dir, row, col = heapq.heappop(heap)

    dr = row
    dc = col
    while True:
        dr += direction_y[dir]
        dc += direction_x[dir]

        if (not is_movable(dr, dc)):
            break

        if (visited[dir][dr][dc]):
            break
        
        visited[dir][dr][dc] = True

        if ((dr, dc) in wall_pos_set):
            break
        
        if ((dr, dc) == goal_door):
            print(m_cnt)
            exit(0)

        if ((dr, dc) in mirror_pos_set):
            heapq.heappush(heap, (m_cnt + 1, rotate_left(dir), dr, dc))
            heapq.heappush(heap, (m_cnt + 1, rotate_right(dir), dr, dc))
