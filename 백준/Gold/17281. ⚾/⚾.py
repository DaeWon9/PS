import sys
from itertools import permutations
input = sys.stdin.readline

# index 0 -> 3

N = int(input())
batter_lists = []
answer = 0

for _ in range(N):
    batter_lists.append(list(map(int, input().split())))

for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8]):
    batter_idx_list = list(perm)[:3] + [0] + list(perm)[3:]
    batter_idx = 0
    perm_score_sum = 0

    for batter_list in batter_lists:
        out_count = 0
        base1 = 0
        base2 = 0
        base3 = 0
        score = 0

        current_batter_idx = batter_idx

        while out_count < 3:
            hit_value = batter_list[batter_idx_list[current_batter_idx]]

            if (hit_value == 0):
                out_count += 1
            elif (hit_value == 1):
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif (hit_value == 2):
                score += (base3 + base2)
                base3 = base1
                base2 = 1
                base1 = 0
            elif (hit_value == 3):
                score += (base1 + base2 + base3)
                base3 = 1
                base1 = 0
                base2 = 0
            else: # 4 홈런
                score += (base1 + base2 + base3 + 1)
                base1 = 0
                base2 = 0
                base3 = 0
            
            current_batter_idx = (current_batter_idx + 1) % 9
        
        batter_idx = current_batter_idx

        perm_score_sum += score

    if (answer < perm_score_sum):
        answer = perm_score_sum

print(answer)
