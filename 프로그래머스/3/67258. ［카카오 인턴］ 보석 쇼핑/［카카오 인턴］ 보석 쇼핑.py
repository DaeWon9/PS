from collections import deque, defaultdict

def solution(gems):
    gem_dict = defaultdict(int)
    answer = []
    result_list = []
    
    gem_set = set(gems)
    
    dq = deque()
    count = 0
    pop_data = 0
    pop_name = ''

    for i in range(len(gems)):
        if (count < len(gem_set)):  
            if (gem_dict[gems[i]] < 1):
                count += 1
            gem_dict[gems[i]] += 1
            dq.append([i, gems[i]])
        else:
            pop_data, pop_name = dq.popleft()
            gem_dict[pop_name] -= 1
            result_list.append([pop_data + 1, len(dq) + pop_data + 1])
            
            if ((len(dq) + pop_data + 1) - (pop_data + 1) + 1 == len(gem_set)):
                break
                
            while(True):
                if(len(dq) < len(gem_set)):
                    break
                if (gem_dict[pop_name] < 1):
                    count -= 1
                    break
                pop_data, pop_name = dq.popleft()
                gem_dict[pop_name] -= 1
            
            result_list.append([pop_data + 1, len(dq) + pop_data + 1])
            
            if (gem_dict[gems[i]] < 1):
                count += 1
                
            gem_dict[gems[i]] += 1
            dq.append([i, gems[i]])
        
        
    if (pop_name == ''):
        pop_name = dq[0][1]

    if (count == len(gem_set)):
        while(len(dq) >= len(gem_set)):
            if (gem_dict[pop_name] < 1):
                result_list.append([pop_data + 1, len(dq) + pop_data + 1])
                break

            pop_data, pop_name = dq.popleft()
            gem_dict[pop_name] -= 1
            
        result_list.append([pop_data + 1, len(dq) + pop_data + 1])
    
    result_list = sorted(result_list, key = lambda x : ((x[1] - x[0]), x[0]))
    answer = result_list[0]
    return answer