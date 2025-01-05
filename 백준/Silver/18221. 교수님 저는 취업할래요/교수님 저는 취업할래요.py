import sys
import math
input = sys.stdin.readline

def calc_distance(s, p):
    return math.sqrt((s[0]-p[0])**2 + (s[1]-p[1])**2)

def count_between_students():
    count = 0
    c1, c2 = min(student_pos[1], professor_pos[1]), max(student_pos[1], professor_pos[1])
    r1, r2 = min(student_pos[0], professor_pos[0]), max(student_pos[0], professor_pos[0])
    for r, c in other_student_pos_set:
        if (r1 <= r <= r2 and c1 <= c <= c2):
            count += 1

        if (count >= 3):
            break
        
    return count

student_pos = ()
professor_pos = ()
other_student_pos_set = set()

N = int(input())
for row in range(N):
    input_data = list(map(int, input().split()))

    for col in range(N):
        if (input_data[col] == 1): # 다른 학생
            other_student_pos_set.add((row, col))
        elif (input_data[col] == 2): # 성규
            student_pos = (row, col)
        elif (input_data[col] == 5): # 교수
            professor_pos = (row, col)

if (calc_distance(student_pos, professor_pos) >= 5 and count_between_students() >= 3):
    print(1)
else:
    print(0)