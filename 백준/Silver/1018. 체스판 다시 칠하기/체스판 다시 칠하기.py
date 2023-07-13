import sys

N, M = map(int, sys.stdin.readline().split())

board = []
result_list = []
start_row = 0
start_col = 0
max_start_row = N - 8
max_start_col = M - 8

# [0,0] [0,1] [0,2] ...
# [1,0] [1,1] [1,2] ...
def get_fill_count(row, col):
    case_1_count = 0
    case_2_count = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if((i + j) % 2 == 0):
                if (board[i][j] == 'B'): # case 1
                    case_1_count += 1
                else: # case 2
                    case_2_count += 1
            else:
                if (board[i][j] == 'W'): # case 1
                    case_1_count += 1
                else: # case 2
                    case_2_count += 1
    return min(case_1_count, case_2_count)

for i in range(N):
    board.append(sys.stdin.readline())

for row in range(start_row, max_start_row + 1):
    for col in range(start_col, max_start_col + 1):
        result_list.append(get_fill_count(row, col))

print(min(result_list))