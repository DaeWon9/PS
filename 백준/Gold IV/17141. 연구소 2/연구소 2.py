import sys
from collections import defaultdict
from itertools import combinations
import heapq
import copy

input = sys.stdin.readline
virus_pos_dict = defaultdict(tuple)
virus_id = 0

N, M = map(int, input().split())
visited = [[False for _ in range(M)] for _ in range(M)]
board = []

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

answer = 2147483647

def is_completed(target_board):
    for row in target_board:
        if 0 in row:
            return False
    return True

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < N):
        return True
    return False

for r in range(N):
    input_data = list(map(int, input().split()))
    
    for c in range(N):
        if (input_data[c] == 2):
            virus_pos_dict[virus_id] = (r, c)
            virus_id += 1
            input_data[c] = 0
    
    board.append(input_data)

for combi in list(combinations(range(virus_id), M)):
    max_time = 1

    copied_board = copy.deepcopy(board)
    heap = []

    initial_virus_visited = [[False for _ in range(N)] for _ in range(N)]
    
    for id in combi:
        virus_r, virus_c = virus_pos_dict[id]
        initial_virus_visited[virus_r][virus_c] = True
        copied_board[virus_r][virus_c] = 1 # set virus

        for index in range(4):
            dr = virus_r + direction_y[index]
            dc = virus_c + direction_x[index]

            if (is_movable(dr, dc) and copied_board[dr][dc] == 0):
                copied_board[dr][dc] = 2
                heapq.heappush(heap, (2, dr, dc)) # initial time : 2
    
    while heap:
        time, row, col = heapq.heappop(heap)

        if(initial_virus_visited[row][col]):
            continue

        if(copied_board[row][col] != 0 and copied_board[row][col] > time):
            continue

        if (max_time < time):
            max_time = time

        for index in range(4):
            dr = row + direction_y[index]
            dc = col + direction_x[index]

            if (is_movable(dr, dc)):
                if (copied_board[dr][dc] == 0):
                    copied_board[dr][dc] = time + 1
                    heapq.heappush(heap, (time + 1, dr, dc))
                    continue

                if(copied_board[dr][dc] != 1 and copied_board[dr][dc] > time + 1):
                    copied_board[dr][dc] = time + 1
                    heapq.heappush(heap, (time + 1, dr, dc))

    if (is_completed(copied_board) and answer > max_time - 1):
        answer = max_time - 1

if (answer == 2147483647):
    print(-1)
else:
    print(answer)