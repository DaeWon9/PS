import sys
from itertools import combinations
from collections import deque, defaultdict
import copy

input = sys.stdin.readline

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < M)

N, M = map(int, input().split())
graph = []
empty_area_dict = defaultdict(tuple)
virus_list = list()
empty_area_id = 0
wall_count = 3

for r in range(N):
    input_data = list(map(int, input().split()))

    for c in range(M):
        if (input_data[c] == 0):
            empty_area_dict[empty_area_id] = (r, c)
            empty_area_id += 1
        elif (input_data[c] == 1):
            wall_count += 1
        else:
            virus_list.append((r, c))

    graph.append(input_data)

default_safety_area_count = (N * M) - wall_count - len(virus_list)
answer = 0

for combi in list(combinations(empty_area_dict.keys(), 3)):
    copied_graph = copy.deepcopy(graph)
    copied_safety_area_count = default_safety_area_count

    for wall in combi:
        wall_pos = empty_area_dict[wall]
        copied_graph[wall_pos[0]][wall_pos[1]] = 1

    queue = deque(virus_list)

    while queue:
        r, c = queue.popleft()

        for index in range(4):
            dr = r + direction_y[index]
            dc = c + direction_x[index]

            if (is_movable(dr, dc) and copied_graph[dr][dc] == 0):
                copied_graph[dr][dc] = 2
                copied_safety_area_count -= 1
                queue.append((dr, dc))

    if (answer < copied_safety_area_count):
        answer = copied_safety_area_count

print(answer)