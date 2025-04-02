import sys
from collections import deque
input = sys.stdin.readline

def is_movable(r, c):
    return (0 <= r and r < N and 0 <= c and c < N)

def change_direction(cur_dir, char):
    if (char == 'L'):
        return (cur_dir + 3) % 4
    return (cur_dir + 1) % 4

direction_r = [0, 1, 0, -1] # 우 하 좌 상
direction_c = [1, 0, -1, 0]

N = int(input())
K = int(input())
apple_pos_set = set()

for _ in range(K):
    r, c = map(int, input().split())
    apple_pos_set.add((r-1, c-1))

L = int(input())
directions = deque()

for _ in range(L):
    t, d = map(str, input().split())
    directions.append((int(t), d))

snake_pos_queue = deque() # tail [...] head
snake_pos_queue.append((0, 0))
cur_dir = 0

status_board = [[False for _ in range(N)] for _ in range(N)]
status_board[0][0] = True

t = 0
while True:
    if (directions and directions[0][0] == t):
        _, char = directions.popleft()
        cur_dir = change_direction(cur_dir, char)

    head_r, head_c = snake_pos_queue[-1]

    nr = head_r + direction_r[cur_dir]
    nc = head_c + direction_c[cur_dir]

    if (not is_movable(nr, nc)): # 벽에 부딪힘
        t += 1
        break

    if (status_board[nr][nc]): # 몸에 부딪힘
        t += 1
        break

    snake_pos_queue.append((nr, nc))
    status_board[nr][nc] = True

    if ((nr, nc) in apple_pos_set):
        apple_pos_set.remove((nr, nc))
    else:
        tail_r, tail_c = snake_pos_queue.popleft()
        status_board[tail_r][tail_c] = False

    t += 1

print(t)