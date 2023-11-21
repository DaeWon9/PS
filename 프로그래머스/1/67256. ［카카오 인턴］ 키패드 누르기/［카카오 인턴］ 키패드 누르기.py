
number_pos_dict = dict()
number_pos_dict[1] = [0,0]
number_pos_dict[2] = [0,1]
number_pos_dict[3] = [0,2]

number_pos_dict[4] = [1,0]
number_pos_dict[5] = [1,1]
number_pos_dict[6] = [1,2]

number_pos_dict[7] = [2,0]
number_pos_dict[8] = [2,1]
number_pos_dict[9] = [2,2]

number_pos_dict['*'] = [3,0]
number_pos_dict[0] = [3,1]
number_pos_dict['#'] = [3,2]


def get_distance(hands_number, target_number):
    #print(type(hands_number), type(target_number))
    pos_1 = number_pos_dict[hands_number]
    pos_2 = number_pos_dict[target_number]
    distance = abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])
    return distance

def get_result_hands(left_distance, right_distance, hand):
    #print(left_distance, right_distance)
    if (left_distance < right_distance):
        return 'left'
    elif (right_distance < left_distance):
        return 'right'
    else:
        return hand


def solution(numbers, hand):
    answer = ''
    current_left_number = '*'
    current_right_number = '#'
    left_hands_number_list = [1,4,7]
    right_hands_number_list = [3,6,9]
    
    for number in numbers:
        # print("cur_left : ", current_left_number)
        # print("cur_right : ", current_right_number)
        # print("nuber : ", number)
        # print("--")
        if number in left_hands_number_list:
            answer += 'L'
            current_left_number = number
            continue
        
        if number in right_hands_number_list:
            answer += 'R'
            current_right_number = number
            continue
            
        left_hand_distance  = get_distance(current_left_number, number)
        right_hand_distance = get_distance(current_right_number, number)
        
        result_hand = get_result_hands(left_hand_distance, right_hand_distance, hand)
        if (result_hand == "left"):
            answer += 'L'
            current_left_number = number
            continue
        else:
            answer += 'R'
            current_right_number = number
            continue
    

    return answer