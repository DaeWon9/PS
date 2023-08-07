import sys
from collections import deque

case_count = int(sys.stdin.readline())

for _ in range(case_count):
    processes = str(sys.stdin.readline().rstrip())
    number_count = int(sys.stdin.readline())
    array = []

    if number_count > 0:
        array = deque(
            tuple(
                map(
                    int,
                    sys.stdin.readline().replace("[", "").replace("]", "").split(","),
                )
            )
        )
    else:
        sys.stdin.readline()

    error_flag = False
    reverse_check = False

    for index in range(len(processes)):
        if processes[index] == "R":
            reverse_check = not reverse_check
        else:
            if len(array) > 0:
                if reverse_check:
                    array.pop()
                else:
                    array.popleft()
            else:
                error_flag = True
                break

    if error_flag:
        print("error")
        continue

    if reverse_check:
        array.reverse()

    print("[", end="")
    for index in range(len(array)):
        if index == len(array) - 1:
            print(array[index], end="")
        else:
            print(array[index], end=",")
    print("]")
