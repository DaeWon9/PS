import sys
from collections import deque


def D(value):
    result = value * 2
    if result > 999:
        result = result % 10000
    return result


def S(value):
    if value == 0:
        return 9999
    return value - 1


def L(value):
    last = value // 1000
    return (value % 1000) * 10 + last


def R(value):
    first = value % 10
    return first * 1000 + (value // 10)


T = int(sys.stdin.readline())

for _ in range(T):
    value, target = map(int, sys.stdin.readline().split())

    queue = deque()
    visited = set()
    queue.append((value, ""))
    visited.add(value)

    while queue:
        current_value, performed_process = queue.popleft()
        if current_value == target:
            print(performed_process)
            break

        temp_value = D(current_value)
        if temp_value not in visited:
            visited.add(temp_value)
            queue.append((temp_value, performed_process + "D"))

        temp_value = S(current_value)
        if temp_value not in visited:
            visited.add(temp_value)
            queue.append((temp_value, performed_process + "S"))

        temp_value = L(current_value)
        if temp_value not in visited:
            visited.add(temp_value)
            queue.append((temp_value, performed_process + "L"))

        temp_value = R(current_value)
        if temp_value not in visited:
            visited.add(temp_value)
            queue.append((temp_value, performed_process + "R"))
