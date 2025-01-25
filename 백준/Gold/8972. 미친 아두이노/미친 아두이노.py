import sys
input = sys.stdin.readline

#보드를 벗어나는 입력은 주어지지 않는다.
def move_arduino(r, c):
    min_dist = 201
    result = (r, c)

    for i in range(1, 10):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        dist = calc_distance(I_pos[0], I_pos[1], dr, dc)

        if (min_dist > dist):
            result = (dr, dc)
            min_dist = dist
            
    return result

def calc_distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

direction_x = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
direction_y = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]

R, C = map(int, input().split())
I_pos = [0, 0]
arduino_pos_set = set()

for r in range(R):
    input_data = input().rstrip()
    for c, data in enumerate(input_data):
        if (data == 'I'):
            I_pos = [r, c]
        if (data == 'R'):
            arduino_pos_set.add((r, c))

move_directions = list(map(int, list(map(str, input().rstrip()))))

for cnt, dir in enumerate(move_directions):
    new_arduino_pos_set = set()
    duplicated_pos_set = set()

    # move I
    I_pos = [I_pos[0] + direction_y[dir], I_pos[1] + direction_x[dir]]

    # move arduinos
    for r, c in arduino_pos_set:
        moved_pos = move_arduino(r, c)

        if (I_pos[0] == moved_pos[0] and I_pos[1] == moved_pos[1]):
            print("kraj", cnt+1)
            exit(0)

        if (moved_pos in new_arduino_pos_set):
            duplicated_pos_set.add(moved_pos)
        else:
            new_arduino_pos_set.add(moved_pos)
        
    arduino_pos_set = new_arduino_pos_set.difference(duplicated_pos_set)

answer = [['.' for _ in range(C)] for _ in range(R)]
answer[I_pos[0]][I_pos[1]] = 'I'
for r, c in arduino_pos_set:
    answer[r][c] = 'R'

for ans in answer:
    print("".join(ans))