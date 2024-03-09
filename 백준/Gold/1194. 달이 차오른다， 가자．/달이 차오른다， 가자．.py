import sys
from collections import deque
input = sys.stdin.readline

key_bit_dict = {
    'a' : 1, 'A' : 1,
    'b' : 2, 'B' : 2,
    'c' : 4, 'C' : 4,
    'd' : 8, 'D' : 8,
    'e' : 16, 'E' : 16,
    'f' : 32, 'F' : 32
}

def is_movable(dr, dc):
    if (0 <= dr < row_size and 0 <= dc < col_size):
        return True
    return False

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]

row_size, col_size = map(int, input().split())
board  = []
M_pos = ()
is_find_M = False
bit_board = [[0 for _ in range(col_size)] for _ in range(row_size)]
visited_board = [[False for _ in range(col_size)] for _ in range(row_size)]

for r in range(row_size):
    input_data = list(map(str, list(input().rstrip())))

    if (not is_find_M):
        for c in range(col_size):
            if (input_data[c] == '0'): # M pos
                M_pos = (r, c)
                input_data[c] = '.'
                is_find_M = True
                visited_board[r][c] = True
                break

    board.append(input_data)

queue = deque()
queue.append((0, 0, M_pos[0], M_pos[1])) # time, key_bit, r, c
while queue:
    time, bit, r, c = queue.popleft()

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc) and board[dr][dc] != '#'):
            if (visited_board[dr][dc] and bit_board[dr][dc] | bit == bit_board[dr][dc]):
                continue
            
            bit_board[dr][dc] = bit

            if (board[dr][dc] == '.'): # move
                visited_board[dr][dc] = True
                queue.append((time + 1, bit_board[dr][dc], dr, dc))

            elif (board[dr][dc] == '1'):
                print(time + 1)
                exit(0)

            elif (str(board[dr][dc]).islower()): # get key
                visited_board[dr][dc] = True
                bit_board[dr][dc] = key_bit_dict[board[dr][dc]] | bit
                queue.append((time + 1, bit_board[dr][dc], dr, dc))

            elif (str(board[dr][dc]).isupper()): # door
                if (bit & key_bit_dict[board[dr][dc]]): # open
                    visited_board[dr][dc] = True
                    queue.append((time + 1, bit, dr, dc))
                
print(-1)