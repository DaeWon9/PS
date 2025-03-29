import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# U, F 만 알아도 나머지는 맵핑되지않나?
# U, F 의 정보로 R 알수있음.
# U, F, R 의 정보만 있으면 주사위를 굴릴 때, 정보 갱신 가능
# D = 7 - U 임.

def is_movable(r, c):
    return 0 <= r < N and 0 <= c < M

def get_D_num(u):
    return 7 - u

def get_R_num(u, f):
    if (u == 1):
        if (f == 5):
            return 3
        elif (f == 3):
            return 2
        elif (f == 2):
            return 4
        else:
            return 5
    elif (u == 2):
        if (f == 1):
            return 3
        elif (f == 3):
            return 6
        elif (f == 6):
            return 4
        else:
            return 1
    elif (u == 3):
        if (f == 1):
            return 5
        elif (f == 2):
            return 1
        elif (f == 5):
            return 6
        else:
            return 2
    elif (u == 4):
        if (f == 1):
            return 2
        elif (f == 2):
            return 6
        elif (f == 5):
            return 1
        else:
            return 5
    elif (u == 5):
        if (f == 1):
            return 4
        elif (f == 3):
            return 1
        elif (f == 4):
            return 6
        else:
            return 3
    else:
        if (f == 2):
            return 3
        elif (f == 3):
            return 5
        elif (f == 4):
            return 2
        else:
            return 4
        
def update_direction(A, B, dir):
    if (A > B):
        return (dir + 1) % 4
    elif (A < B):
        return (dir + 3) % 4
    else:
        return dir

def flip_direction(dir):
    return (dir + 2) % 4

def relocation():
    global cur_u, cur_f, cur_r, cur_dir

    if (cur_dir == 0): # 동
        cur_u = get_D_num(cur_r)
    elif (cur_dir == 2): #서
        cur_u = cur_r
    elif (cur_dir == 1): #남
        temp = cur_f
        cur_f = cur_u
        cur_u = get_D_num(temp)
    else: # 북
        temp = cur_u
        cur_u = cur_f
        cur_f = get_D_num(temp)

    cur_r = get_R_num(cur_u, cur_f)

def update_score():
    global score
    target_num = board[pos_r][pos_c]
    target_idx = get_idx(pos_r, pos_c)
    
    score += target_num * count_dict[parent[target_idx]]

def get_idx(r, c):
    return r * M + c

def initial_groupping():
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for r in range(N):
        for c in range(M):
            if (not visited[r][c]):
                queue = deque()
                queue.append((r, c))
                target_idx = get_idx(r, c)
                target_num = board[r][c]
                visited[r][c] = True
                count = 1

                while queue:
                    rr, cc = queue.popleft()
                    
                    for i in range(4):
                        nr = rr + direction_r[i]
                        nc = cc + direction_c[i]

                        if (is_movable(nr, nc) and not visited[nr][nc] and board[nr][nc] == target_num):
                            idx = get_idx(nr, nc)
                            parent[idx] = target_idx
                            queue.append((nr, nc))
                            visited[nr][nc] = True
                            count += 1
                
                count_dict[target_idx] = count

def roll_dice():
    global cur_u, cur_f, cur_r, cur_dir, pos_r, pos_c
    new_pos_r = pos_r + direction_r[cur_dir]
    new_pos_c = pos_c + direction_c[cur_dir]

    if (not is_movable(new_pos_r, new_pos_c)):
        cur_dir = flip_direction(cur_dir)
        new_pos_r = pos_r + direction_r[cur_dir]
        new_pos_c = pos_c + direction_c[cur_dir]

    pos_r = new_pos_r
    pos_c = new_pos_c
    
    relocation()

    update_score()

    cur_dir = update_direction(get_D_num(cur_u), board[pos_r][pos_c], cur_dir)

cur_u = 1
cur_f = 5
cur_r = 3
cur_dir = 0

pos_r = 0
pos_c = 0

score = 0
count_dict = defaultdict(int)

direction_c = [1, 0, -1, 0]
direction_r = [0, 1, 0, -1]

N, M, K = map(int, input().split())
board = []
parent = [i for i in range(N * M)]

for _ in range(N):
    board.append(list(map(int, input().split())))

initial_groupping()

for _ in range(K):
    roll_dice()

print(score)