import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))
array.sort()

combis = permutations(array, m)
for combi in combis:
    for num in combi:
        print(num, end=" ")

    print()
