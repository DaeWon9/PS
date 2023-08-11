import sys

array = [1, 1, 1, 2, 2]

def solution(target_num):
    if len(array) >= target_num:
        print(array[target_num - 1])
    else:
        for _ in range(target_num - len(array)):
            new_value = array[len(array) - 3] + array[len(array) - 2]
            array.append(new_value)

        print(array[target_num - 1])


n = int(sys.stdin.readline())

for _ in range(n):
    solution(int(sys.stdin.readline()))