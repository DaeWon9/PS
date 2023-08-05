from collections import defaultdict

def solution(id_list, report, k):
    report = set(report)  
    reported_count_dict = defaultdict(int)
    result_dict = defaultdict(int)
    reported_user_list = []
    answer = []
    
    for user in id_list:
        reported_count_dict[user] = 0
        result_dict[user] = 0
        
    for reported_user in report:
        reported_count_dict[reported_user.split()[1]] += 1
    
    for user in id_list:
        if (reported_count_dict[user] >= k):
            reported_user_list.append(user)
    
    for reported_user in report:
        if (reported_user.split()[1] in reported_user_list):
            result_dict[reported_user.split()[0]] += 1
            
    for user in id_list:
        answer.append(result_dict[user])
    
    return answer