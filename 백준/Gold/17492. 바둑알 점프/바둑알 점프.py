import sys
import copy
input = sys.stdin.readline

direction_x = [0, 1, 1, 1, 0 ,-1, -1, -1] 
direction_y = [-1, -1, 0, 1, 1, 1, 0, -1]

def is_in(dr, dc):
    if (0 <= dr < N and 0 <= dc < N):
        return True
    return False

def is_jumpable(dr, dc, dir, current_stone_set):
    if (not is_in(dr, dc)):
        return False
    
    if ((dr, dc) in wall_pos_set):
        return False
    
    if ((dr, dc) not in current_stone_set):
        return False
    
    next_dr = dr + direction_y[dir]
    next_dc = dc + direction_x[dir]

    if (not is_in(next_dr, next_dc)):
        return False
    
    if ((next_dr, next_dc) in wall_pos_set):
        return False
    
    if ((next_dr, next_dc) not in current_stone_set):
        return True
    
    return False


def solution(current_stone_set : set):
    if (len(current_stone_set) == 1):
        print("Possible")
        exit(0)

    for stone_r, stone_c in current_stone_set:
        for i in range(8):
            dr = stone_r + direction_y[i]
            dc = stone_c + direction_x[i]

            if (is_jumpable(dr, dc, i, current_stone_set)):
                copied_set = copy.deepcopy(current_stone_set)
                copied_set.remove((dr, dc))
                copied_set.remove((stone_r, stone_c))
                copied_set.add((dr + direction_y[i], dc + direction_x[i]))
                solution(copied_set)

N = int(input())
baduk_stone_pos_set = set()
wall_pos_set = set()

for r in range(N):
    input_data = list(map(int, input().split()))

    for c, data in enumerate(input_data):
        if (data == 1): # wall
            wall_pos_set.add((r, c))
        elif (data == 2): # baduk_stone
            baduk_stone_pos_set.add((r, c))

solution(baduk_stone_pos_set)
print("Impossible")