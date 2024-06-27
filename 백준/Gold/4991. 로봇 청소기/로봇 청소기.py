import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def is_movable(dr, dc, w, h):
    if (0 <= dr < h and 0 <= dc < w):
        return True
    return False

def calc_dist(w, h, current_robot_pos, target_dust_pos):
    direction_x = [1, -1, 0, 0]
    direction_y = [0, 0, 1, -1]
    
    r, c = current_robot_pos
    visited = set()
    queue = deque()
    queue.append((r, c, 0))
    visited.add(current_robot_pos)

    while queue:
        r, c, t = queue.popleft()

        if ((r, c) == target_dust_pos):
            return t

        for i in range(4):
            dr = r + direction_y[i]
            dc = c + direction_x[i]

            if (is_movable(dr, dc, w, h) and (dr, dc) not in furniture_pos_list and (dr, dc) not in visited):
                queue.append((dr, dc, t + 1))
                visited.add((dr, dc))
    
    return -1

while True:
    w, h = map(int, input().split())

    if (w == 0 and h == 0):
        break
    
    answer = 2147483647
    dust_id = 1
    dust_count = 0
    robot_pos = ()

    furniture_pos_list = []
    dust_id_list = []
    dust_id_dict = defaultdict()

    dist_hash = [[[[0 for _ in range(w)] for _ in range(h)] for _ in range(w)] for _ in range(h)]

    for r in range(h):
        input_data = list(input().rstrip())
        
        for c, ch in enumerate(input_data):
            if (ch == 'o'):
                robot_pos = (r, c)
                dust_id_dict[(r, c)] = 0
            elif (ch == '*'):
                dust_id_dict[(r, c)] = dust_id
                dust_id_dict[dust_id] = (r, c)
                dust_count += 1
                dust_id_list.append(dust_id)
                dust_id *= 2
            elif (ch == 'x'):
                furniture_pos_list.append((r, c))
    
    max_bit = (2 ** dust_count) - 1

    queue = deque()
    queue.append((0, 0, robot_pos))

    while queue:
        bit, count, cur_pos = queue.popleft()

        if (count >= answer):
            continue

        if (bit == max_bit and answer > count):
            answer = count

        for dust in dust_id_list:
            new_bit = dust | bit
            if (new_bit == bit):
                continue
            
            cur_r, cur_c = cur_pos
            dust_r, dust_c = dust_id_dict[dust]

            if (dist_hash[cur_r][cur_c][dust_r][dust_c] != 0): # 대칭은 항상 존재
                dist = dist_hash[cur_r][cur_c][dust_r][dust_c]
            else:
                dist = calc_dist(w, h, cur_pos, dust_id_dict[dust])
                dist_hash[cur_r][cur_c][dust_r][dust_c] = dist
                dist_hash[dust_r][dust_c][cur_r][cur_c] = dist
            
            if (dist > 0):
                queue.append((new_bit, count + dist, dust_id_dict[dust]))
                
    if (answer == 2147483647 or answer < 0):
        print(-1)
    else:
        print(answer)