import sys
from itertools import combinations
input = sys.stdin.readline

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < N)

def find_obstacle_pos_set(row, col):
    result_set = set()

    for dr, dc in directions:
        i = 1
        while True:
            nr = row + dr * i
            nc = col + dc * i

            if (not is_movable(nr, nc)):
                break

            if ((nr, nc) in student_pos_set):
                break

            if ((nr, nc) in obstacle_pos_set):
                break

            if ((nr, nc) in teacher_pos_set):
                for j in range(1, i):
                    result_set.add((row + dr * j, col + dc * j))
                break

            i += 1

    return result_set

def is_answer(obstacles: set):
    for row, col in student_pos_set:
        for dr, dc in directions:
            i = 1
            while True:
                nr = row + dr * i
                nc = col + dc * i

                if (not is_movable(nr, nc)):
                    break

                if ((nr, nc) in student_pos_set):
                    break

                if ((nr, nc) in obstacles):
                    break

                if ((nr, nc) in teacher_pos_set):
                    return False

                i += 1

    return True

N = int(input())
teacher_pos_set = set()
student_pos_set = set()
obstacle_pos_set = set()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for row in range(N):
    input_data = list(map(str, input().rstrip().split()))
    for col, data in enumerate(input_data):
        if (data == 'T'):
            teacher_pos_set.add((row, col))
        elif (data == 'S'):
            student_pos_set.add((row, col))

for row, col in student_pos_set:
    for pos_set in find_obstacle_pos_set(row, col):
        obstacle_pos_set.add(pos_set)

for combi in combinations(obstacle_pos_set, min(len(obstacle_pos_set), 3)):
    if (is_answer(combi)):
        print('YES')
        exit(0)

print('NO')