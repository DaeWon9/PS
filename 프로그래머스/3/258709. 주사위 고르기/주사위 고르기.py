from collections import defaultdict
from itertools import combinations, product
from bisect import bisect_left, bisect_right

# 주사위에 id 부여
# 주사위가 2N개라면, N개의 묶음 조합으로 A주사위 select -> 자동으로 B주사위 지정
# 각 case별로 승리하는 횟수를 저장해두기. -> max 일 때, answer

dice_info_dict = defaultdict(list)

def get_a_win_count(a_dice_set, b_dice_set, dice_len):
    win_count_per_sum_value = defaultdict(lambda : -1)
    
    all_a_dice_list = []
    all_b_dice_list = []
    a_dice_value_list = []
    b_dice_value_list = []
    win_count = 0
    
    for a_dice in a_dice_set:
        all_a_dice_list.append(dice_info_dict[a_dice])
    
    for b_dice in b_dice_set:
        all_b_dice_list.append(dice_info_dict[b_dice])
        
    for data in product(*all_a_dice_list):
        a_dice_value_list.append(sum(data))
    
    for data in product(*all_b_dice_list):
        b_dice_value_list.append(sum(data))
    
    a_dice_value_list.sort()
    b_dice_value_list.sort()
    max_len = len(b_dice_value_list)
    
    # 이분탐색으로 큰 개수 찾기 + 메모아이제이션
    for i in range(max_len):
        a_value = a_dice_value_list[i]

        if (win_count_per_sum_value[a_value] != -1):
            win_count += win_count_per_sum_value[a_value]
            continue
        
        if (b_dice_value_list[-1] < a_value):
            win_count += max_len
            win_count_per_sum_value[a_value] = max_len
            continue
            
        count = bisect_left(b_dice_value_list, a_value)
        win_count += count
        win_count_per_sum_value[a_value] = count
    
    return win_count
        
def solution(dice):
    dice_len = len(dice)
    combination_count = dice_len // 2 # dice_len은 2의 배수
    all_dice_set = set()
    max_count = 0
    answer = []
    
    for id, dice_info in enumerate(dice):
        dice_info_dict[id + 1] = dice_info
        all_dice_set.add(id + 1)
    
    for a_dice_set in list(combinations(range(1, dice_len + 1), combination_count)):
        b_dice_set = all_dice_set.difference(a_dice_set)
        win_count = get_a_win_count(a_dice_set, b_dice_set, combination_count)
        
        if (max_count < win_count):
            max_count = win_count
            answer = a_dice_set
        
    return answer