import sys
from itertools import combinations

N = int(sys.stdin.readline())
ingredient_info = []
result_list = []

for _ in range(N):
    ingredient_info.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1,N+1):
    for combi in list(combinations(range(N), i)):
        sour_value = 1
        bitter_value = 0
        for index in combi:
            sour_value = sour_value * ingredient_info[index][0]
            bitter_value = bitter_value + ingredient_info[index][1]

        result_list.append(abs(sour_value - bitter_value))

print(min(result_list))