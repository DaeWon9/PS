import re
from itertools import permutations
import copy

def solution(expression):
    result_list = []
    
    exist_operator_list = []
    if ('+' in expression):
        exist_operator_list.append('+')
    if ('-' in expression):
        exist_operator_list.append('-')
    if ('*' in expression):
        exist_operator_list.append('*')
        
    exist_operator_list = set(exist_operator_list)
    
    permutation_list = permutations(exist_operator_list, len(exist_operator_list))
    
    operator_list = re.sub('[0-9]', ' ', expression)
    operator_list = list(map(str, operator_list.split()))
    
    operator_info = []
    for i in range(len(operator_list)):
        operator_info.append((operator_list[i], i , i + 1))
    
    number_list = re.sub('[^0-9]', ' ', expression)
    number_list = list(map(int, number_list.split()))
    
    
    for priority in permutation_list:
        temp_number_list = copy.deepcopy(number_list)
        temp_operator_list = copy.deepcopy(operator_list)
        
        for operator in priority:
            i = 0
            while(True):
                if (i >= len(temp_operator_list)):
                    break
                if (temp_operator_list[i] == operator):
                    sub_result = 0
                    if (operator == '*'):
                        sub_result = temp_number_list[i] * temp_number_list[i+1]
                    elif (operator == '+'):
                        sub_result = temp_number_list[i] + temp_number_list[i+1]
                    elif (operator == '-'):
                        sub_result = temp_number_list[i] - temp_number_list[i+1]
                    
                    temp_number_list[i+1] = sub_result
                    temp_number_list.pop(i)
                    temp_operator_list.pop(i)
                    i -= 1
                i += 1
        
        result_list.append(abs(temp_number_list[0]))
    
    answer = max(result_list)
    return answer