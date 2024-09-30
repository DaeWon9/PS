import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

# 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격
# 각 궁수를 기준으로 bfs로 가장 가까운 적의 위치 탐색
# 탐색할때 좌측부터 (좌, 상, 우)

direction_x = [-1, 0, 1]
direction_y = [0, -1, 0]

def calc_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < M)

def find_nearest_enemy(b, row, col):
    queue = deque()
    visited = set()

    queue.append((row, col))
    visited.add((row, col))

    while queue:
        r, c = queue.popleft()

        for idx in range(3):
            dr = r + direction_y[idx]
            dc = c + direction_x[idx]
            distance = calc_distance(row, col, dr, dc)

            if (is_movable(dr, dc) and (dr, dc) not in visited and distance <= D):
                if (b[dr][dc] == 1): # find enemy
                    return (dr, dc)
                else:
                    queue.append((dr, dc))
                
                visited.add((dr, dc))
    
    return (-1, -1)

board = []

N, M, D = map(int, input().split())
for _ in range(N):
    board.append(list(map(int, input().split())))
    
enemy_count = sum(row.count(1) for row in board)
archer_row = N
answer = 0

for archer_case in list(combinations(range(M), 3)):
    remain_enemy = enemy_count
    copied_board = copy.deepcopy(board)
    attack_count = 0

    while(remain_enemy > 0):
        target_enemy_set = set()

        for archer_col in archer_case:
            target_enemy = find_nearest_enemy(copied_board, archer_row, archer_col)

            if (target_enemy[0] == -1):
                continue

            target_enemy_set.add(target_enemy)

        for enemy_row, enemy_col in target_enemy_set:
            copied_board[enemy_row][enemy_col] = 0
            remain_enemy -= 1
            attack_count += 1

        remain_enemy -= copied_board[-1].count(1)

        copied_board.pop()
        copied_board.insert(0, [0 for _ in range(M)])
    
    if (answer < attack_count):
        answer = attack_count

print(answer)