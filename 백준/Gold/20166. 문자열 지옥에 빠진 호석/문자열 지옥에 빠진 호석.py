import sys
input = sys.stdin.readline

direction_x = [0, 1, 1, 1, 0, -1, -1, -1]  # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
direction_y = [-1, -1, 0, 1, 1, 1, 0, -1]

def interpolate_pos(row, col):
    row = (row + N) % N
    col = (col + M) % M
    return (row, col)

def find_str(row, col, target, idx):
    global dp

    if idx == len(target):
        return 1  # 목표 문자열을 모두 찾았을 경우 1을 반환

    if dp[row][col][idx] != -1:
        return dp[row][col][idx]  # 이미 계산된 값이 있으면 해당 값을 반환

    dp[row][col][idx] = 0
    for d in range(8):  # 8방향 탐색
        dr = row + direction_y[d]
        dc = col + direction_x[d]

        dr, dc = interpolate_pos(dr, dc)

        if board[dr][dc] == target[idx]:
            dp[row][col][idx] += find_str(dr, dc, target, idx + 1)

    return dp[row][col][idx]

N, M, K = map(int, input().split())

board = []
wish_str = []

for _ in range(N):
    board.append(list(input().rstrip()))

for _ in range(K):
    wish_str.append(input().rstrip())

for wish in wish_str:
    answer = 0
    dp = [[[-1] * len(wish) for _ in range(M)] for _ in range(N)]  # 메모이제이션을 위한 DP 배열
    for r in range(N):
        for c in range(M):
            if board[r][c] == wish[0]:  # 시작 문자가 맞는 경우에만 탐색
                answer += find_str(r, c, wish, 1)

    print(answer)