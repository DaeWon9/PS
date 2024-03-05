import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < 8 and 0 <= dc < 8):
        return True
    return False

board = []
queue = deque()

visited = [[False for _ in range(8)] for _ in range(8)]

direction_x = [0, 0, -1, 1, -1, 1, 1, -1] # 그대로 상 좌 우 좌상 우상 하 우하 좌하
direction_y = [0, -1, 0, 0, -1, -1, 1, 1]

for r in range(8):
    input_data = list(map(str, list(input().rstrip())))
    for c in range(8):
        if (input_data[c] == '#'): 
            queue.appendleft(('W', r, c))
    board.append(input_data)

queue.appendleft(('O', 7, 0))

before_target = 'O'

while queue:
    target, r, c = queue.popleft()

    if (target == 'W'):
        before_target = 'W'
        if (r == 7):
            board[r][c] = '.'
            continue
        board[r][c] = '.'
        board[r + 1][c] = '#'
        queue.append(('W', r + 1, c))
        continue

    if (before_target == 'W'):
        visited = [[False for _ in range(8)] for _ in range(8)]
        before_target = 'O'

    if (board[r][c] == '#'):
        continue

    if(r == 0 and c == 7):
        print(1)
        exit(0)
    
    for i in range(8):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc) and board[dr][dc] == '.' and not visited[dr][dc]):
            queue.append(('O', dr, dc))
            visited[dr][dc] = True

print(0)