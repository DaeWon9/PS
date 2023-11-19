from itertools import product, combinations_with_replacement

def isMatch(base_id, target_id):
    if (len(base_id) != len(target_id)):
        return False
    
    for index in range(len(base_id)):
        if (target_id[index] == '*'):
            continue
        if (target_id[index] != base_id[index]):
            return False
    
    return True

def solution(user_id, banned_id):    
    base_data = [[] for _ in range(len(banned_id))]
    
    for index in range(len(banned_id)):
        for user in user_id:
            if (isMatch(user, banned_id[index])):
                base_data[index].append(user)
            
    combination = list(product(*base_data))
    
    result_list = []
    base_len = len(base_data)
    
    for combo in combination:
        set_combo = set(combo)
        if (len(set_combo) == base_len):
            if (set_combo not in result_list):
                result_list.append(set_combo)
            
    
    answer = len(result_list)
        
    return answer