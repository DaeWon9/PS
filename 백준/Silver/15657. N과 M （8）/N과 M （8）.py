import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))
array.sort()

combis = combinations_with_replacement(array, m)
for combi in combis:
    for num in combi:
        print(num, end=" ")

    print()
