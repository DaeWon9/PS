import sys
from collections import defaultdict

word_bindo_dict = defaultdict(int)
result_set = set()
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    input_word = sys.stdin.readline().rstrip()

    if (len(input_word) < m):
        continue

    word_bindo_dict[input_word] += 1
    result_set.add(input_word)

result_set = list(result_set)
result_set.sort(key = lambda x : [-word_bindo_dict[x], -len(x), x])

for word in result_set:
    print(word)