from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
bad_combination = [[False for _ in range(N)] for _ in range(N)]
count = 0

icecream_set = [i for i in range(N)]

for _ in range(M):
    bad_1, bad_2 = map(int, sys.stdin.readline().rstrip().split())
    bad_combination[bad_1-1][bad_2-1] = True
    bad_combination[bad_2-1][bad_1-1] = True

for set in combinations(icecream_set, 3):
    if bad_combination[set[0]][set[1]] or bad_combination[set[0]][set[2]] or bad_combination[set[1]][set[2]]:
        continue
    else:
        count = count + 1

print(count)
