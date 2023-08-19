import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

array = []

for i in range(1, n + 1):
    array.append(i)

combis = combinations_with_replacement(array, m)
for combi in combis:
    for num in combi:
        print(num, end=" ")

    print()
