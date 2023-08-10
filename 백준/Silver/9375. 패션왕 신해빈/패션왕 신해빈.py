import sys
from collections import defaultdict

n = int(sys.stdin.readline())

for _ in range(n):
    clothes_dict = defaultdict(int)
    clothes_count = int(sys.stdin.readline())

    for _ in range(clothes_count):
        item, type = map(str, sys.stdin.readline().rstrip().split())
        clothes_dict[type] += 1

    values = list(clothes_dict.values())
    count = 1

    for value in values:
        count *= value + 1

    print(count - 1)