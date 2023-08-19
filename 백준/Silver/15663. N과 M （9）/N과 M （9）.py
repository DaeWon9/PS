import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))
array.sort()

combis = list(set(list(permutations(array, m))))
combis.sort()
for combi in combis:
    for num in combi:
        print(num, end=" ")

    print()
