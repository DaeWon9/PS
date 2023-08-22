import sys

direction_x = [0, 0, -1, 1]
directoin_y = [-1, 1, 0, 0]

R, C = map(int, sys.stdin.readline().split())

board = []
for _ in range(R):
    board.append(sys.stdin.readline().rstrip())

queue = set()
queue.add((0, 0, board[0][0]))

answer = 1

while queue:
    row, col, alphabet = queue.pop()
    for index in range(4):
        dr = row + directoin_y[index]
        dc = col + direction_x[index]
        if ((0 <= dr < R) and (0 <= dc < C)) and (board[dr][dc] not in alphabet):
            queue.add((dr, dc, alphabet + board[dr][dc]))
            answer = max(answer, len(alphabet) + 1)

print(answer)