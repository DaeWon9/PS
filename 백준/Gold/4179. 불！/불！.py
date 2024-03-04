import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < R and 0 <= dc < C):
        return True
    return False

def is_border(dr, dc):
    if (dr == 0 or dr == R-1 or dc == 0 or dc == C-1):
        return True
    return False

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

R, C = map(int, input().split())
queue = deque()
J_pos = ()
board = []
visited = [[False for _ in range(C)] for _ in range(R)]

for r in range(R):
    input_data = list(map(str, list(input().rstrip())))

    for c in range(C):
        if input_data[c] == 'J':
            J_pos = (r, c)
            visited[r][c] = True
        if input_data[c] == 'F':
            queue.append(('F', r, c, 0)) # fire pos append
            visited[r][c] = True

    board.append(input_data)

queue.append(('J', J_pos[0], J_pos[1], 0))

while queue:
    target, r, c, time = queue.popleft()

    if (target == 'J' and is_border(r, c)):
        print(time + 1)
        exit(0)

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc) and not visited[dr][dc] and board[dr][dc] == '.'):
            if (target == 'J'):
                queue.append(('J', dr, dc, time + 1))
                visited[dr][dc] = True
            else: # fire
                board[dr][dc] = 'F'
                queue.append(('F', dr, dc, time + 1))
                visited[dr][dc] = True

print('IMPOSSIBLE')