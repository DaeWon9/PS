import sys
input = sys.stdin.readline

def solution(input_string):
    case_1_string = '-1'
    case_1_flag = True
    case_2_string = '-1'
    case_2_flag = True

    left_index = 0
    right_index = len(input_string) - 1

    while left_index < right_index:
        if (input_string[left_index] != input_string[right_index]):
            if (left_index + 1 <= right_index and input_string[left_index + 1] == input_string[right_index]):
                case_1_string = input_string[left_index + 2:right_index]

            if (left_index <= right_index - 1 and input_string[left_index] == input_string[right_index - 1]):
                case_2_string = input_string[left_index + 1:right_index - 1]
            
            if (case_1_string != '-1' or case_2_string != '-1'):
                break
            return 2
        else:
            left_index += 1
            right_index -= 1
    
    if case_1_string != '-1':
        left_index = 0
        right_index = len(case_1_string) - 1

        while left_index < right_index:
            if (case_1_string[left_index] != case_1_string[right_index]):
                case_1_flag = False
                break
            left_index += 1
            right_index -= 1

    if case_2_string != '-1':
        left_index = 0
        right_index = len(case_2_string) - 1

        while left_index < right_index:
            if (case_2_string[left_index] != case_2_string[right_index]):
                case_2_flag = False
                break
            left_index += 1
            right_index -= 1

    if (case_1_string != '-1' and case_2_string != '-1'):
        if (case_1_flag or case_2_flag):
            return 1
        return 2

    if (case_1_string != '-1'):
        if (case_1_flag):
            return 1
        else:
            return 2
        
    if (case_2_string != '-1'):
        if (case_2_flag):
            return 1
        else:
            return 2

    return 0

T = int(input())

for _ in range(T):
    input_string = input().rstrip()
    print(solution(input_string))
