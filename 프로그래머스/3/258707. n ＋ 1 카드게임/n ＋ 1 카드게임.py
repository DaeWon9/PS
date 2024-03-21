from itertools import combinations

def get_pair_card(cur_card_list, target_sum):
    list_len = len(cur_card_list)
    for pivot in range(list_len):
        for match in range(pivot + 1, list_len):
            if (cur_card_list[pivot] + cur_card_list[match] == target_sum):
                return [pivot, match]
    return [-1, -1]

def get_priority(card_num, target_sum, cur_card_list):
    matched_card = target_sum - card_num
    if (matched_card in cur_card_list):
        return 2
    return 0
        
def solution(coin, cards):
    n = len(cards)
    target_sum = n + 1
    init_card_size = n // 3
    cur_card_list = cards[:init_card_size]
    card_index = init_card_size
    answer = 1
    
    usable_card_list = []
    
    while True:
        if (card_index > n - 1):
            break
            
        card1 = cards[card_index]
        card_index += 1
        card2 = cards[card_index]
        card_index += 1
        
        usable_card_list.append(card1)
        usable_card_list.append(card2)
        
        pair_card = get_pair_card(cur_card_list, target_sum)
        
        is_pass = False
        
        if (pair_card[0] != -1): # 새로운 카드를 넣지 않아도 다음단계 진행이 되는경우
            pass
        else: # 새로운 카드를 넣지 않으면 게임 진행이 불가
            if (coin >= 1):
                for u_card in usable_card_list:
                    priority = get_priority(u_card, target_sum, cur_card_list)

                    if (priority == 2):
                        cur_card_list.append(u_card)
                        usable_card_list.remove(u_card)
                        coin -= 1
                        is_pass = True
                        break
                    
            # 위에서 해결이 안됐다면 2장을 뽑아서 내야함.
        
            if (not is_pass and coin >= 2):
                for id1, id2 in list(combinations(range(len(usable_card_list)), 2)):
                    if (usable_card_list[id1] + usable_card_list[id2] == target_sum):
                        cur_card_list.append(usable_card_list[id1])
                        cur_card_list.append(usable_card_list[id2])
                        
                        if (id1 < id2): # id1 이 항상 크도록 설정
                            id1, id2 = id2, id1
                        
                        usable_card_list.pop(id1)
                        usable_card_list.pop(id2)
                        coin -= 2
                        break
                
        pair_card = get_pair_card(cur_card_list, target_sum)
        
        if (pair_card[0] == -1):
            break

        index_1 = pair_card[0]
        index_2 = pair_card[1]
        
        if (index_1 < index_2): # index_1 이 항상 크도록 설정
            index_1, index_2 = index_2, index_1
        
        cur_card_list.pop(index_1)
        cur_card_list.pop(index_2)

        answer += 1
    
    return answer