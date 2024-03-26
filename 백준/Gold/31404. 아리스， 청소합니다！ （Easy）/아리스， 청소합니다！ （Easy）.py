import sys
from collections import deque
input = sys.stdin.readline

direction_x = [0, 1, 0, -1]
direction_y = [-1, 0, 1, 0]

def calc_index(r, c, d):
    return (r * W + c) * 4 + d

def find(x):
    if (parent[x] == x):
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return
    
    parent[y] = x
    rank[x] += rank[y]

def is_movable(dr, dc):
    if (0 <= dr < H and 0 <= dc < W):
        return True
    return False

def solution():
    global current_r, current_c, current_d
    answer = 0
    b_count = 0

    while True:
        if (not is_movable(current_r, current_c)):
            return answer

        if (clear_board[current_r][current_c]): # RULE_B
            start_index = calc_index(current_r, current_c, current_d)

            storage = deque([start_index])
            is_first_visit = True

            while (is_movable(current_r, current_c) and clear_board[current_r][current_c]):
                current_index = calc_index(current_r, current_c, current_d)

                if (not is_first_visit and current_index == start_index):
                    return answer
                
                root = find(current_index)

                if (root == current_index):
                    b_count += 1
                    current_d = (current_d + rule_b[current_r][current_c]) % 4
                    current_r += direction_y[current_d]
                    current_c += direction_x[current_d]
                    storage.append(calc_index(current_r, current_c, current_d))
                else:
                    current_r = root // (4 * W)
                    current_c = root // 4 % W
                    current_d = root % 4
                    b_count += rank[root] - 1
                    storage.append(root)

                is_first_visit = False

            if (not is_movable(current_r, current_c)):
                return answer
            
            while True:
                x = storage.pop()
                y = storage.pop()
                union(x, y)
                if (not storage):
                    break
                storage.append(y)
        else:
            clear_board[current_r][current_c] = True
            current_d = (current_d + rule_a[current_r][current_c]) % 4
            current_r += direction_y[current_d]
            current_c += direction_x[current_d]
            answer += (b_count + 1)
            b_count = 0

H, W = map(int, input().split())
current_r, current_c, current_d = map(int, input().split())

parent = [i for i in range(H * W * 4)] # 4방향 별
rank = [1 for _ in range(H * W * 4)]

clear_board = [[False for _ in range(W)] for _ in range(H)]
rule_a = []
rule_b = []

for _ in range(H):
    rule_a.append(list(map(int, str(input().rstrip()))))

for _ in range(H):
    rule_b.append(list(map(int, str(input().rstrip()))))

print(solution())