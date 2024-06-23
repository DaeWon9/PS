import sys
from collections import Counter
input = sys.stdin.readline

key_list = ['R', 'G', 'B', 'Y', '*']

init_string = input().rstrip()
goal_string = input().rstrip()

init_count = Counter(init_string)
goal_count = Counter(goal_string)
answer = 0

for key in key_list:
    answer += abs(init_count[key] - goal_count[key])

print(answer // 2)