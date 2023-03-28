import sys
from itertools import combinations
from collections import Counter

target_string = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
book_list = []
min_sum = 100000 * 16

for i in range(N):
    book_list.append(list(map(str, sys.stdin.readline().rstrip().split())))

book_list.sort(key = lambda x : x[0])

target_string_counter = Counter(target_string)
target_string_set = set(target_string)
book_count = 1
is_find = False
while(True):
    book_combination = list(combinations(book_list, book_count))
    for combination in book_combination:    
        counter = Counter(str(combination))
        isIncluded = True
        for key in target_string_set:
            if (target_string_counter[key] > counter[key]):
                isIncluded = False
                break
        if (isIncluded):
            is_find = True
            sum = 0
            for book in combination:
                sum = sum + int(book[0])
            min_sum = min(sum, min_sum)

    if (book_count == N):
        break
    book_count = book_count + 1

if (is_find):
    print(min_sum)
else:
    print(-1)