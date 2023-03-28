import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card_list = []
result_set = set()

for _ in range(n):
    card_list.append(int(sys.stdin.readline()))

card_combination = list(permutations(card_list,k))

for combination in card_combination:
    result = ""
    for key in combination:
        result = result + str(key)
    result_set.add(result)

print(len(result_set))