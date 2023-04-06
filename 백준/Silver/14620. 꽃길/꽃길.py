import sys
from itertools import combinations

N = int(sys.stdin.readline())
cost_map = []
seed_cost_sum_list = []

min_cost = 200 * 5 * 3

for _ in range(N):
    cost_map.append(list(map(int, sys.stdin.readline().rstrip().split())))

for row in range(1, N-1):
    for col in range(1, N-1):
        sum = cost_map[row][col] + cost_map[row][col+1] + cost_map[row][col-1] + cost_map[row-1][col] + cost_map[row+1][col]
        seed_cost_sum_list.append([sum, row, col])


for combi in list(combinations(seed_cost_sum_list, 3)):
    sum = 0
    occupy_map = []
    is_overlap = False
    for seed in combi:
        sum = sum + seed[0]
        if ([seed[1], seed[2]] in occupy_map):
            is_overlap = True
            break
        occupy_map.append([seed[1], seed[2]])

        if ([seed[1] + 1, seed[2]] in occupy_map):
            is_overlap = True
            break
        occupy_map.append([seed[1] + 1, seed[2]])

        if ([seed[1] - 1, seed[2]] in occupy_map):
            is_overlap = True
            break
        occupy_map.append([seed[1] - 1, seed[2]])

        if ([seed[1], seed[2] + 1] in occupy_map):
            is_overlap = True
            break
        occupy_map.append([seed[1], seed[2] + 1])

        if ([seed[1], seed[2] - 1] in occupy_map):
            is_overlap = True
            break
        occupy_map.append([seed[1], seed[2] - 1])

    if (not is_overlap):
        min_cost = min(min_cost, sum)

print(min_cost)