# gift 0: 선물을 준 사람 , 1 : 선물을 받은 사람

from collections import defaultdict
from itertools import combinations

gift_value = defaultdict(int)
get_gift_info = defaultdict(int)
give_gift_info = defaultdict(int)

result_info = defaultdict(int)

def solution(friends, gifts):
    for gift in gifts: # v1이 준사람, v2가 받은사람
        v1, v2 = gift.split()
        gift_value[v1] += 1
        gift_value[v2] -= 1
        
        get_gift_info[(v2, v1)] += 1
        give_gift_info[(v1, v2)] += 1
        
    
    for pivot, match in list(combinations(friends, 2)):
        print(pivot, match)
        match_give_value = give_gift_info[(match, pivot)]
        pivot_give_value = give_gift_info[(pivot, match)]

        if (match_give_value == pivot_give_value or (match_give_value == 0 and pivot_give_value == 0)):
            pivot_gift_value = gift_value[pivot]
            match_gift_value = gift_value[match]
            
            print(pivot_gift_value, match_gift_value)

            if (pivot_gift_value == match_gift_value):
                continue
            elif (pivot_gift_value > match_gift_value):
                result_info[pivot] += 1
            else:
                result_info[match] += 1
        else:
            if (match_give_value > pivot_give_value):
                result_info[match] += 1
            else:
                result_info[pivot] += 1
        

    result = list(result_info.values())
    if (not result):
        return 0
    
    return max(result)