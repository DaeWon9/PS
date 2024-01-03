import sys
from collections import deque

def get_target_puyo(target_board, visited):
    for row in range(5, -1, -1):
        for col in range(12):
            if (target_board[row][col] != '.' and not visited[row][col]):
                return [target_board[row][col], row, col]

def is_movable(dr, dc):
    if (0 <= dr < 6 and 0 <= dc < 12):
        return True
    return False

answer = 0

board = []
transpose_board = []

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

queue = deque()

for row in range(12):
    board.append(list(sys.stdin.readline().rstrip()))

for col in range(6):
    temp_col = []
    for row in range(12):
        temp_col.append(board[row][col])
    transpose_board.append(temp_col)
    
while(True):
    visited = [[False for _ in range(12)] for _ in range(6)]
    is_generated_boom = False

    while(True):
        target_puyo = get_target_puyo(transpose_board, visited)
        if target_puyo == None:
            break

        queue.append(target_puyo)

        adjacent_puyo_index_list = []
        adjacent_puyo_count = 0 # 타겟 뿌요에 대한 인접뿌요 카운트

        while(queue):
            color, row, col = queue.popleft()
            visited[row][col] = True
            adjacent_puyo_index_list.append([row, col])

            for index in range(4): # 4방향
                dr = row + direction_y[index]
                dc = col + direction_x[index]

                if (is_movable(dr, dc) and not visited[dr][dc] and transpose_board[dr][dc] == color):
                    visited[dr][dc] = True
                    queue.append((color, dr, dc))
                    adjacent_puyo_count += 1
        
        if adjacent_puyo_count >= 3:
            is_generated_boom = True
            for index in adjacent_puyo_index_list:
                transpose_board[index[0]][index[1]] = '.'

    if (not is_generated_boom):
        break

    # borad 재배치
    for row in transpose_board:
        row.sort(key = lambda x : x != '.')
    
    answer += 1

print(answer)