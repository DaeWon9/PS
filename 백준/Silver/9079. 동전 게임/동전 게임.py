from collections import deque
import sys

input = sys.stdin.readline

# 다 같은 면인지 확인
def check_same(board):
    temp = board[0][0]
    for i in range(3):
        for j in range(3):
            if board[i][j] != temp:
                return False
    return True

# 중복 확인을 위해 2진수의 10진수값 계산
def calculate(board):
    score = 0
    for i in range(3):
        for j in range(3):
            score = score * 2 + board[i][j]
    return score

# 값을 다시 그래프로 변환
def score_to_board(score):
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            board[i][j] = score % 2
            score = score // 2

    return board

# bfs
def find_arr(board):
    global ans
    q = deque()
    score_arr = []

    score = calculate(board)

    q.append((score, 0))

    while q:
        # next_board, count = q.popleft()
        score, count = q.popleft()
        # print(score_arr)

        next_board = score_to_board(score)

        if check_same(next_board):
            ans = count
            return

        # 행 변환 (3가지)
        for i in range(3):
            for j in range(3):
                next_board[i][j] = 0 if next_board[i][j] == 1 else 1
                
            # print(next_board)
            next_score = calculate(next_board)
            if next_score not in score_arr:
                score_arr.append(next_score)
                q.append((next_score, count+1))

            for j in range(3):
                next_board[i][j] = 0 if next_board[i][j] == 1 else 1

        # 열 변환 (3가지)
        for i in range(3):
            for j in range(3):
                next_board[j][i] = 0 if next_board[j][i] == 1 else 1
            
            next_score = calculate(next_board)
            if next_score not in score_arr:
                score_arr.append(next_score)
                q.append((next_score, count+1))

            for j in range(3):
                next_board[j][i] = 0 if next_board[j][i] == 1 else 1
            
        # 대각선 변환 (2가지)
        for i in range(3):
            next_board[i][i] = 0 if next_board[i][i] == 1 else 1

        next_score = calculate(next_board)
        if next_score not in score_arr:
            score_arr.append(next_score)
            q.append((next_score, count+1))

        for i in range(3):
            next_board[i][i] = 0 if next_board[i][i] == 1 else 1

        for i in range(3):
            next_board[2-i][i] = 0 if next_board[2-i][i] == 1 else 1

        next_score = calculate(next_board)
        if next_score not in score_arr:
            score_arr.append(next_score)
            q.append((next_score, count+1))

        for i in range(3):
            next_board[2-i][i] = 0 if next_board[2-i][i] == 1 else 1

    ans = -1

T = int(input())
for _ in range(T):
    board = []
    for i in range(3):
        temp = list(input().split())
        for j in range(3):
            if temp[j] == 'T':
                temp[j] = 1
            else:
                temp[j] = 0
        board.append(temp)
    ans = 0

    find_arr(board)
    print(ans)