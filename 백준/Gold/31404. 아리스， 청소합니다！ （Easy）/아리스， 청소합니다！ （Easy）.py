import sys
from collections import deque
input = sys.stdin.readline

def calaculate_index(r, c):
    return r * W + c
    
direction_x = [0, 1, 0, -1] # 상 우 하 좌 (시계방향)
direction_y = [-1, 0, 1, 0]

def is_movable(dr, dc):
    if (0 <= dr < H and 0 <= dc < W):
        return True
    return False

def solution():
    global answer, b_count, parent

    while queue:
        current_r, current_c, current_d = queue.pop()
        is_rule_b = False
        new_direction = 0

        if (clear_board[current_r][current_c]): # RULE_B
            b_count += 1
            is_rule_b = True
            new_direction = (current_d + rule_b[current_r][current_c]) % 4

            if (path_start_index == -1):
                next_index_set.clear()
                path_start_index = calaculate_index(current_r, current_c)

        else: # RULE_A
            answer += (b_count + 1)
            b_count = 0
            clear_board[current_r][current_c] = True
            new_direction = (current_d + rule_a[current_r][current_c]) % 4
            path_start_index = -1

        dr = current_r + direction_y[new_direction]
        dc = current_c + direction_x[new_direction]

        if (is_movable(dr, dc)):
            if (is_rule_b):
                current_index = calaculate_index(current_r, current_c)
                next_index = calaculate_index(dr, dc)

                if (current_index != path_start_index):
                    queue.append((dr, dc, new_direction))
                    continue
                
                if (next_index in next_index_set):
                    break
                
                next_index_set.add(next_index)
                
            queue.append((dr, dc, new_direction))
        else:
            break

H, W = map(int, input().split())
R, C, D = map(int, input().split())

clear_board = [[False for _ in range(W)] for _ in range(H)]

path_start_index = -1
next_index_set = set()

rule_a = []
rule_b = []

for _ in range(H):
    rule_a.append(list(map(int, str(input().rstrip()))))

for _ in range(H):
    rule_b.append(list(map(int, str(input().rstrip()))))

queue = deque()
queue.append((R, C, D))
answer = 0
b_count = 0

solution()

print(answer)