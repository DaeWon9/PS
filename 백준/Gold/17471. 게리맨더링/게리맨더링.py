import sys
from itertools import combinations
from collections import defaultdict, deque
input = sys.stdin.readline

def is_connected(vertex_set: set):
    if (len(vertex_set) == 1):
        return True
    
    visited = set()
    queue = deque()
    pivot = next(iter(vertex_set))
    queue.append(pivot)
    visited.add(pivot)

    while queue:
        v = queue.popleft()

        for adj_vertex in adj_vertices[v]:
            if (adj_vertex not in vertex_set):
                continue

            if (adj_vertex in visited):
                continue

            visited.add(adj_vertex)
            queue.append(adj_vertex)
    
    return vertex_set == visited

N = int(input())
population_list = [0] + list(map(int, input().split()))
adj_vertices = defaultdict(list)
all_set = set(range(1, N+1))
answer = 2147483647

for id in range(1, N+1):
    input_data = list(map(int, input().split()))

    for data in input_data[1:]:
        adj_vertices[id].append(data)

for pivot_count in range(1, N//2 + 1):
    for red_team in list(combinations(range(1, N+1), pivot_count)):
        red_team = set(red_team)
        blue_team = all_set.difference(red_team)

        is_red_team_connected = is_connected(red_team)
        is_blue_team_connected = is_connected(blue_team)

        if (not is_red_team_connected or not is_blue_team_connected):
            continue

        red_team_sum = 0
        blue_team_sum = 0

        for red in red_team:
            red_team_sum += population_list[red]
        
        for blue in blue_team:
            blue_team_sum += population_list[blue]

        diff = abs(red_team_sum - blue_team_sum)

        if (answer > diff):
            answer = diff

if (answer == 2147483647):
    print(-1)
else:
    print(answer)