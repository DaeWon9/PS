import sys
from collections import deque
input = sys.stdin.readline

direction_x = [0, 1, 1, 1, 0, -1, -1, -1]
direction_y = [-1, -1, 0, 1, 1, 1, 0, -1]

def is_movable(dr, dc):
    return 0 <= dr < N and 0 <= dc < N

def spring_and_summer():
    global tree_queue
    new_tree_queue = deque()
    died_tree_queue = deque()
    for age, row, col in tree_queue:
        if (board[row][col] >= age):  # 살아남는 경우
            board[row][col] -= age
            new_tree_queue.append((age + 1, row, col))
        else:  # 죽는 경우
            died_tree_queue.append((age, row, col))

    while died_tree_queue:
        age, row, col = died_tree_queue.popleft()
        board[row][col] += age // 2

    tree_queue = new_tree_queue

def fall_and_winter():
    global tree_queue
    new_tree_queue = deque(tree_queue)
    for age, row, col in tree_queue:
        if (age % 5 == 0):  # 번식 조건
            for j in range(8):
                dr, dc = row + direction_y[j], col + direction_x[j]
                if (is_movable(dr, dc)):
                    new_tree_queue.appendleft((1, dr, dc))

    tree_queue = new_tree_queue

    for r in range(N):
        for c in range(N):
            board[r][c] += A[r][c]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]
tree_queue = deque()
for _ in range(M):
    row, col, age = map(int, input().split())
    tree_queue.append((age, row-1, col-1))

for _ in range(K):
    spring_and_summer()
    fall_and_winter()

print(len(tree_queue))
