import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def is_movable(dr, dc):
    if 0 <= dr < N and 0 <= dc < M:
        return True
    return False

def zero_bfs(r, c):
    global group_id
    
    group_id += 1 # 새로운 그룹id 지정
    queue = deque()
    queue.append((r, c))

    zero_group[r][c] = group_id
    count = 1

    while queue:
        r, c = queue.popleft()

        for index in range(4):
            dr = r + direction_y[index]
            dc = c + direction_x[index]

            if (not is_movable(dr, dc)): # 이동 불가일 경우
                continue

            if (board[dr][dc] == '1'): # 1일경우
                continue

            if (zero_group[dr][dc]): # 이미 다른그룹에 속해있는 0 이면
                continue

            zero_group[dr][dc] = group_id
            queue.append((dr, dc))
            count += 1

    zero_group_value[group_id] = count

def solution(r, c): 
    global group_id

    visited_group_set = set()
    count_sum = 1
    
    for index in range(4):
        dr = r + direction_y[index]
        dc = c + direction_x[index]   

        if (not is_movable(dr, dc)):
            continue
        
        if (board[dr][dc] == '1'):
            continue

        id = zero_group[dr][dc]
        visited_group_set.add(id)

    for group_id in visited_group_set:
        count_sum += zero_group_value[group_id]

    board[r][c] = str(count_sum % 10)
    
direction_x = [1, 0, 0, -1]
direction_y = [0, -1, 1, 0]

N, M = map(int, input().split())
board = []

zero_group = [[0 for _ in range(M)] for _ in range(N)] # 각 좌표별 그룹 아이디 지정
zero_group_value = defaultdict(int)
group_id = 0

for _ in range(N):
    board.append(list(input().rstrip()))

for r in range(N):
    for c in range(M):
        if (board[r][c] == '0' and zero_group[r][c] == 0):
            zero_bfs(r, c)

for r in range(N):
    for c in range(M):
        if (board[r][c] == '1'):
            solution(r, c)

for row in board:
    print(''.join(row))