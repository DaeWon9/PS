from collections import deque, defaultdict

def isIndexValidate(row, col, size):
    if (row >= 0 and row < size and col >=0 and col < size):
        return True
    return False

def isCorner(prev_dir, next_dir):
    if (prev_dir == 0 and (next_dir == 1 or next_dir == 3)):
        return True
    
    if (prev_dir == 1 and (next_dir == 0 or next_dir == 2)):
        return True
    
    if (prev_dir == 2 and (next_dir == 1 or next_dir == 3)):
        return True
    
    if (prev_dir == 3 and (next_dir == 0 or next_dir == 2)):
        return True
    
    return False

directions = [[0, 1], [1, 0] , [0, -1], [-1, 0]] # 하, 우, 상, 좌

def bfs(board, queue, cost_board):
    board_size = len(board)
    while(queue):
        row, col, direction, cost = queue.pop()
        
        for dir_index in range(4):
            dc = col + directions[dir_index][0]
            dr = row + directions[dir_index][1]
            # 유효 인덱스 + 벽아님
            if(isIndexValidate(dr, dc, board_size) and board[dr][dc] == 0): 
                # dr, dc로 이동시 나오는 요금 계산
                sub_cost = cost
                if (isCorner(direction, dir_index)):
                    sub_cost += 600
                else:
                    sub_cost += 100
                
                # 기존의 요금 보드와 비교하며 해당 움직임으로 인한 비용이
                # 최솟값일 경우 보드를 업데이트 후 queue.append
                if (sub_cost < cost_board[dir_index][dr][dc]):
                    cost_board[dir_index][dr][dc] = sub_cost
                    queue.appendleft([dr, dc, dir_index, sub_cost])


def solution(board):
    answer = 0
    
    cost_board = [[[2147483647] * len(board) for _ in range(len(board))] for _ in range(4)]
    
    queue = deque()
    queue.append([0, 0, 0, 0]) # row, col, dir, cost
    queue.append([0, 0, 1, 0])
    
    bfs(board, queue, cost_board)
    
    
    result = min(cost_board[0][-1][-1], cost_board[1][-1][-1], cost_board[2][-1][-1], cost_board[3][-1][-1])
    
    return result