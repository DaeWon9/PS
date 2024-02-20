import sys
from collections import defaultdict
input = sys.stdin.readline

gate_count = int(input())
plane_count = int(input())

gate_state = [False for _ in range(gate_count + 1)]
last_gate_dict = defaultdict(int)
answer = 0

for _ in range(plane_count):
    plane_id = int(input())
    is_possible = False

    start_gate = plane_id
    if (last_gate_dict[plane_id] != 0):
        start_gate = last_gate_dict[plane_id]

    for id in range(start_gate, 0, -1):
        if (not gate_state[id]):
            gate_state[id] = True
            last_gate_dict[plane_id] = id
            answer += 1
            is_possible = True
            break

    if (not is_possible):
        break

print(answer)