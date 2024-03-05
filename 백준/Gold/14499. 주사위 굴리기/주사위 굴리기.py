import sys
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < M):
        return True
    return False

def get_reverse_index(index):
    return 7 - index

def move(direction):
    if (direction == 1):
        move_east()
    elif (direction == 2):
        move_west()
    elif (direction == 3):
        move_north()
    else:
        move_south()

def move_east():
    tmep = dice_index['u']
    dice_index['u'] = get_reverse_index(dice_index['r'])
    dice_index['r'] = tmep

def move_west():
    temp = dice_index['u']
    dice_index['u'] = dice_index['r']
    dice_index['r'] = get_reverse_index(temp)

def move_north():
    temp = dice_index['u']
    dice_index['u'] = dice_index['f']
    dice_index['f'] = get_reverse_index(temp)

def move_south():
    temp = dice_index['u']
    dice_index['u'] = get_reverse_index(dice_index['f'])
    dice_index['f'] = temp

dice_index = {
    'u' : 1,
    'r' : 3,
    'f' : 5
}

dice_value = [0] * 7
direction_x = [0, 1, -1, 0, 0] # 동 서 북 남
direction_y = [0, 0, 0, -1, 1]

N, M, r, c, K = map(int, input().split())
board = []
move_list = []

for _ in range(N):
    board.append(list(map(int, input().split())))

direction_list = list(map(int, input().split()))

for direction in direction_list:
    dr = r + direction_y[direction]
    dc = c + direction_x[direction]

    if (is_movable(dr, dc)):
        move(direction)
        print(dice_value[dice_index['u']])
        
        dice_bottom_index = get_reverse_index(dice_index['u'])

        if (board[dr][dc] == 0):
            board[dr][dc] = dice_value[dice_bottom_index]
        else:
            dice_value[dice_bottom_index] = board[dr][dc]
            board[dr][dc] = 0

        r = dr
        c = dc
