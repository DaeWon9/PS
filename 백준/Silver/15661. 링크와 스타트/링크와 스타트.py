import sys
from itertools import combinations

N = int(sys.stdin.readline())
whole_member = set([ i for i in range(N)])
array = []
min_value = 20*100

def get_score(teams, array):
    sum = 0
    for i in teams:
        for j in teams:
            sum = sum + array[i][j]

    return sum

for row in range(N):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(2, N//2+1):
    for combi in list(combinations(range(N), i)):
        start_team = combi
        link_team = whole_member - set(combi)

        min_value = min(min_value, abs(get_score(start_team, array) - get_score(link_team, array)))

print(min_value)