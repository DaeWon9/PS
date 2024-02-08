import sys
import heapq
from collections import deque, defaultdict
input = sys.stdin.readline

direction_x = [1, 0, -1, 0]
direction_y = [0, 1, 0, -1]

def is_movable(n, dr, dc):
    if 0 <= dr < n and 0 <= dc < n:
        return True
    return False

def solution(n, board):
    rupee_board = [[2147483647 for _ in range(n)] for _ in range(n)]
    rupee_board[0][0] = board[0][0]

    heap = []
    heapq.heappush(heap, (board[0][0], 0, 0))

    while heap:
        rupee, row, col = heapq.heappop(heap)

        if (row == n-1 and col == n-1):
            return rupee

        if (rupee_board[row][col] < rupee):
             continue
        
        for i in range(4):
            dr = row + direction_y[i]
            dc = col + direction_x[i]

            if (is_movable(n, dr, dc) and rupee_board[row][col] + board[dr][dc] < rupee_board[dr][dc]):
                rupee_board[dr][dc] = rupee_board[row][col] + board[dr][dc]
                heapq.heappush(heap, (rupee_board[dr][dc], dr, dc))

problem_id = 1

while True:
    n = int(input())
    
    if (n == 0):
        break

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    print("Problem " + str(problem_id) + ": " + str(solution(n, board)))
    problem_id += 1
