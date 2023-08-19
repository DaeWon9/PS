import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))
array.sort()

combis = list(set(list(combinations_with_replacement(array, m))))
combis.sort()
for combi in combis:
    for num in combi:
        print(num, end=" ")

    print()
