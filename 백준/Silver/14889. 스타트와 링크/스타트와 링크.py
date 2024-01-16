import sys
from itertools import combinations

def calculate_team_value(team_id_set):
    value = 0

    for id_set in list(combinations(team_id_set, 2)):
        id1, id2 = id_set
        value += graph[id1][id2]
        value += graph[id2][id1]

    return value

N = int(sys.stdin.readline())

graph = []
whole_id_set = set()
min_diff = 2147483647

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    whole_id_set.add(i)

for start_team in list(combinations(whole_id_set, int(N/2))):
    start_team_set = set(start_team)
    link_team_set = whole_id_set - start_team_set

    start_team_value = calculate_team_value(start_team_set)
    link_team_value = calculate_team_value(link_team_set)

    value_diff = abs(start_team_value - link_team_value)
    if (value_diff < min_diff):
        min_diff = value_diff
    
    if (min_diff == 0):
        break

print(min_diff)
