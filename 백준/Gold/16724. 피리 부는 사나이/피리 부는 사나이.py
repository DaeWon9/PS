import sys
from collections import deque
input = sys.stdin.readline

r_size, c_size = map(int, input().split())
board = []
for i in range(r_size):
    board.append(list(input().rstrip()))

dir = 'UDRL'

def calc_dr_dc(r, c):
    direction = board[r][c]
    dr = r
    dc = c

    if direction == 'U':
        dr -= 1
    elif direction == 'D':
        dr += 1
    elif direction == 'R':
        dc += 1
    else: # L
        dc -= 1

    return [dr, dc]


def dfs(r, c, flag):
    queue = deque()
    queue.append((r, c))

    last_visited = [(r,c), (r,c)]
    while queue:
        current_r, current_c = queue.pop()
        dr, dc = calc_dr_dc(current_r, current_c)
   
        board[current_r][current_c] = str(flag) 
        last_visited = [(current_r, current_c), (dr, dc)]

        if board[dr][dc] in dir: # not visited
            queue.append((dr, dc))

    first_r, first_c = last_visited[0]
    second_r, second_c = last_visited[1]

    if board[first_r][first_c] == board[second_r][second_c]: # same cycle
        return 1
    else:
        return 0
    
flag = 0
cnt = 0
for r in range(r_size):
    for c in range(c_size):
        if board[r][c] in dir:
            cnt += dfs(r, c, flag)
            flag += 1
print(cnt)