import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    return (0 <= dr < H and 0 <= dc < W)

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

W, H = map(int, input().split())
C_pos_list = list()
board = []

for r in range(H):
    input_data = input().rstrip()

    for c, data in enumerate(input_data):
        if (data == 'C'):
            C_pos_list.append((r, c))

    board.append(input_data)

start_pos = C_pos_list[0]
end_pos = C_pos_list[1]

queue = deque()
queue.append((start_pos[0], start_pos[1], -1, 0))
mirror_count = [[[9999 for _ in range(W)] for _ in range(H)] for _ in range(4)]
mirror_count[0][start_pos[0]][start_pos[1]] = 0
mirror_count[1][start_pos[0]][start_pos[1]] = 0
mirror_count[2][start_pos[0]][start_pos[1]] = 0
mirror_count[3][start_pos[0]][start_pos[1]] = 0

while queue:
    r, c, p, cnt = queue.popleft()

    if (mirror_count[p][r][c] < cnt):
        continue

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (not is_movable(dr, dc)):
            continue

        if (board[dr][dc] == '*'):
            continue

        if ((p == -1 or p == i) and mirror_count[i][dr][dc] > cnt):
            mirror_count[i][dr][dc] = cnt
            queue.append((dr, dc, i, cnt))
        elif (mirror_count[i][dr][dc] > cnt+1):
            mirror_count[i][dr][dc] = cnt + 1
            queue.append((dr, dc, i, cnt + 1))

answer = min(mirror_count[0][end_pos[0]][end_pos[1]],
            mirror_count[1][end_pos[0]][end_pos[1]],
            mirror_count[2][end_pos[0]][end_pos[1]],
            mirror_count[3][end_pos[0]][end_pos[1]])

print(answer)
