import sys

N = int(sys.stdin.readline())
direction_x = [1, 0, -1, 0]
direction_y = [0, -1, 0, 1]

dragon_curve_map = [[False for _ in range(101)] for _ in range(101)] # 인덱스 0~100까지 유효

def get_reverse_direction(d):
    return (d + 2) % 4
    
def get_rotate_direction(d):
    return (d + 1) % 4

def dragon_curve(x, y, d, g):
    curve_direction = [d]
    if (g > 0):
        curve_direction.append(get_rotate_direction(d))
        for _ in range(g-1):
            reverse_count = len(curve_direction) // 2 #reverse direction 의 개수는 이전 커브수의 절반
            for i in range(reverse_count):
                curve_direction.append(get_reverse_direction(curve_direction[i]))
            for i in range(reverse_count):
                curve_direction.append(curve_direction[i + reverse_count])
    
    start_x = x
    start_y = y
    dragon_curve_map[x][y] = True
    for index in curve_direction:
        start_x += direction_x[index]
        start_y += direction_y[index]
        dragon_curve_map[start_x][start_y] = True


def count_rectangle():
    count = 0
    for row in range(100):
        for col in range(100):
            if dragon_curve_map[row][col] and dragon_curve_map[row + 1][col]and dragon_curve_map[row][col + 1] and dragon_curve_map[row + 1][col + 1]:
                count+=1
    return count

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().rstrip().split())
    dragon_curve(x, y, d, g)

print(count_rectangle())