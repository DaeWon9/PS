import sys
from collections import deque
input = sys.stdin.readline

direction_x = [0, 1, 0, -1] # 상 우 하 좌 (시계방향)
direction_y = [-1, 0, 1, 0]

def is_movable(dr, dc):
    if (0 <= dr <= H - 1 and 0 <= dc <= W - 1):
        return True
    return False

def solution():
    global answer, b_count, visted_board
    while queue:
        current_r, current_c, current_d = queue.pop()
        is_rule_b = False
        new_direction = 0
        if (clear_board[current_r][current_c]): # RULE_B
            b_count += 1
            is_rule_b = True
            new_direction = (current_d + int(rule_b[current_r][current_c])) % 4
        else: # RULE_A
            answer += 1
            answer += b_count
            b_count = 0
            clear_board[current_r][current_c] = True
            new_direction = (current_d + int(rule_a[current_r][current_c])) % 4
            visted_board = [[[] for _ in range(W)] for _ in range(H)]
            
        dr = current_r + direction_y[new_direction]
        dc = current_c + direction_x[new_direction]

        if (is_movable(dr, dc)):
            if (is_rule_b):
                if (new_direction in visted_board[dr][dc]):
                    break
                else:
                    visted_board[dr][dc].append(new_direction)
            queue.append((dr, dc, new_direction))
        else:
            break


H, W = map(int, input().split())
R, C, D = map(int, input().split())

clear_board = [[False for _ in range(W)] for _ in range(H)]
visted_board = [[[] for _ in range(W)] for _ in range(H)]

rule_a = []
rule_b = []

for _ in range(H):
    rule_a.append(input().rstrip())

for _ in range(H):
    rule_b.append(input().rstrip())

queue = deque()
queue.append((R, C, D))
answer = 0
b_count = 0

solution()

print(answer)