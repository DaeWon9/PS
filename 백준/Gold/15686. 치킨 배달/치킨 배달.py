import sys
from itertools import combinations
input = sys.stdin.readline

def calc_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

N, M = map(int, input().split())

house_position = list()
whole_chicken_position = list()
answer = 2147483647

for row in range(N):
    input_data = map(int, input().split())

    for col, data in enumerate(input_data):
        if (data == 1):
            house_position.append((row, col))
        elif (data == 2):
            whole_chicken_position.append((row, col))

for chicken_pair in list(combinations(whole_chicken_position, M)):
    chicken_dist_sum = 0
    for r1, c1 in house_position:
        min_dist = 2147483647
        for r2, c2 in chicken_pair:
            temp_dist = calc_distance(r1, c1, r2, c2)
            if (min_dist > temp_dist):
                min_dist = temp_dist
        
        chicken_dist_sum += min_dist
    
    if (answer > chicken_dist_sum):
        answer = chicken_dist_sum

print(answer)