import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split()))
score_list = [0 for _ in range(N)]
appear_card_dict = defaultdict(bool)
card_index_dict = defaultdict(int)

for index, card in enumerate(card_list):
    appear_card_dict[card] = True
    card_index_dict[card] = index

for card in card_list:
    count = 2
    while count * card < 1000001:
        if (appear_card_dict[count * card]):
            score_list[card_index_dict[card]] += 1
            score_list[card_index_dict[count * card]] -= 1

        count += 1

for score in score_list:
    print(score, end=' ')