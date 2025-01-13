import sys
from itertools import combinations
input = sys.stdin.readline

default_char = {'a', 'n', 't', 'i', 'c'}

N, K = map(int, input().split())
char_to_bit = {chr(i): 1 << (i - ord('a')) for i in range(ord('a'), ord('z') + 1)}
word_bit_list = []
all_char_bit = 0

for _ in range(N):
    word = input().rstrip()
    word_bit = 0

    for char in set(word) - default_char:
        word_bit |= char_to_bit[char]
        all_char_bit |= char_to_bit[char]

    word_bit_list.append(word_bit)

if (K < 5):
    print(0)
    exit()

base_bit = sum(char_to_bit[char] for char in default_char)
all_chars = [char for char in range(26) if (1 << char) & all_char_bit]
answer = 0

for combi in combinations(all_chars, min(len(all_chars), K - 5)):
    combi_bit = base_bit
    for char in combi:
        combi_bit |= (1 << char)

    temp_answer = 0
    for word_bit in word_bit_list:
        if (word_bit & combi_bit == word_bit):
            temp_answer += 1

    if (answer < temp_answer):
        answer = temp_answer

print(answer)
