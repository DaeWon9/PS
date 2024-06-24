import sys
input = sys.stdin.readline

def is_movable(dr, dc):
    if (dr >= 0 and dr < n and dc >= 0 and dc < m):
        return True
    return False

queen_dir_r = [-1, -1, 0, 1, 1, 1, 0, -1]
queen_dir_c = [0, 1, 1, 1, 0, -1, -1, -1]
knight_dir_r = [-2, -2, -1, 1, 2, 2, -1, 1]
knight_dir_c = [-1, 1, 2, 2, -1, 1, -2, -2]

n, m = map(int, input().split())
board = [[True for _ in range(m)] for _ in range(n)]

obstacle_pos = set()

queen_pos = []
input_data = list(map(int, input().split()))
for i in range(input_data[0]): 
    r = input_data[i * 2 + 1] - 1
    c = input_data[i * 2 + 2] - 1
    queen_pos.append((r, c))
    obstacle_pos.add((r, c))
    board[r][c] = False

knight_pos = []
input_data = list(map(int, input().split()))
for i in range(input_data[0]):
    r = input_data[i * 2 + 1] - 1
    c = input_data[i * 2 + 2] - 1
    knight_pos.append((r, c))
    obstacle_pos.add((r, c))
    board[r][c] = False

input_data = list(map(int, input().split()))
for i in range(input_data[0]):
    r = input_data[i * 2 + 1] - 1
    c = input_data[i * 2 + 2] - 1
    obstacle_pos.add((r, c))
    board[r][c] = False

for r, c in queen_pos:
    for i in range(8):
        count = 1
        while(True):
            dr = r + queen_dir_r[i] * count
            dc = c + queen_dir_c[i] * count

            if (is_movable(dr, dc)):
                if ((dr, dc) not in obstacle_pos):
                    board[dr][dc] = False
                    count += 1
                else:
                    break
            else:
                break

for r, c in knight_pos:
    for i in range(8):
        dr = r + knight_dir_r[i]
        dc = c + knight_dir_c[i]

        if (is_movable(dr, dc) and board[dr][dc] and (dr, dc) not in obstacle_pos):
            board[dr][dc] = False

answer = 0
for b in board:
    answer += b.count(True)
print(answer)