import sys
from collections import deque
input = sys.stdin.readline

def is_movable(r, c):
    return 0 <= r < N and 0 <= c < M

N, M = map(int, input().split())

land_poses = []
board = []
direction_r = [1, -1, 0, 0]
direction_c = [0, 0, 1, -1]
answer = 0

for r in range(N):
    input_data = input().rstrip()

    for c in range(M):
        data = input_data[c]

        if (data == 'L'):
            land_poses.append((r, c))

    board.append(input_data)

for sr, sc in land_poses:
    visited = set()
    visited.add((sr, sc))

    queue = deque()
    queue.append((0, sr, sc))

    while queue:
        d, r, c = queue.popleft()
        answer = max(answer, d)

        for i in range(4):
            nr = r + direction_r[i]
            nc = c + direction_c[i]

            if (not is_movable(nr, nc)):
                continue

            if ((nr, nc) in visited):
                continue

            if (board[nr][nc] == 'L'):
                queue.append((d+1, nr, nc))
                visited.add((nr, nc))

print(answer)