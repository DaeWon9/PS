import sys
from collections import deque
input = sys.stdin.readline

def convert_dir(dir):
    if (dir == 1):
        return 1
    if (dir == 2):
        return 3
    if (dir == 3):
        return 2
    if (dir == 4):
        return 0

def turn_reverse(dir):
    return (dir + 2) % 4

def turn_left(dir):
    return (dir + 3) % 4

def turn_right(dir):
    return (dir + 1) % 4

def is_movable(r, c):
    return (0 <= r < M and 0 <= c and c < N)

dr = [-1, 0, 1, 0] # 북 동 남 서
dc = [0, 1, 0, -1]

M, N = map(int, input().split()) # 세로M 가로N
board = []

for _ in range(M):
    board.append(list(map(int, input().split())))

robot_pos = list(map(int, input().split()))
goal_pos = list(map(int, input().split()))

robot_pos[0] -= 1
robot_pos[1] -= 1
robot_pos[2] = convert_dir(robot_pos[2])

goal_pos[0] -= 1
goal_pos[1] -= 1
goal_pos[2] = convert_dir(goal_pos[2])

queue = deque()
queue.append((0, robot_pos[0], robot_pos[1], robot_pos[2]))

# 방향별 기록
dp = [[[float("inf") for _ in range(4)] for _ in range(N)] for _ in range(M)]
dp[robot_pos[0]][robot_pos[1]][robot_pos[2]] = 0

while queue:
    t, r, c, d = queue.popleft()

    if (goal_pos[0] == r and goal_pos[1] == c and goal_pos[2] == d):
        print(t)
        break

    if (dp[r][c][d] < t):
        continue

    # 현재 방향으로 직진
    nr = r
    nc = c
    for _ in range(3):
        nr += dr[d]
        nc += dc[d]

        if (not is_movable(nr, nc)):
            break

        if (board[nr][nc] == 1):
            break

        if (dp[nr][nc][d] > t+1):
            dp[nr][nc][d] = t+1
            queue.append((t+1, nr, nc, d))
    
    # 우측으로 돌기
    nd = turn_right(d)
    if (dp[r][c][nd] > t+1):
        dp[r][c][d] = t+1
        queue.append((t+1, r, c, nd))

    # 좌측으로 돌기
    nd = turn_left(d)
    if (dp[r][c][nd] > t+1):
        dp[r][c][d] = t+1
        queue.append((t+1, r, c, nd))

    # 반대방향으로 돌기
    nd = turn_reverse(d)
    if (dp[r][c][nd] > t+2):
        dp[r][c][d] = t+2
        queue.append((t+2, r, c, nd))
