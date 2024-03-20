# 5개를 캔 후 사용불가
# 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용
# 광물순서대로 캐야함.
# 모든광물을 캐거나, 곡괭이가 없을 때 break
# 최소한의 피로도 return

fatigue_info = [ # 0 : dia, 1 :iron, 2 : stone
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1]
]

mineral_index_dict = {
    'diamond' : 0,
    'iron' : 1,
    'stone' : 2
}

priority_mineral_dict = {
    'diamond' : 25,
    'iron' : 5,
    'stone' : 1
}

def solution(picks, minerals):
    answer = 0
    
    priority_list = []
    pick_order_list = [-1 for _ in range(len(minerals) // 5 + 1)]
    
    count = 0
    priority_value = 0
    idx = 0
    for mineral in minerals:
        if (count == 5):
            priority_list.append((priority_value, idx))
            count = 0
            priority_value = 0
            idx += 1
        priority_value += priority_mineral_dict[mineral]
        count += 1
        
    if (count != 0):
        priority_list.append((priority_value, idx))
        
    priority_list.sort(key = lambda x : (-x[0], x[1]))
    
    for priority, id in priority_list:
        if (picks[0] > 0):
            pick_order_list[id] = 0
            picks[0] -= 1
            continue
        
        if (picks[1] > 0):
            pick_order_list[id] = 1
            picks[1] -= 1
            continue
            
        if (picks[2] > 0):
            pick_order_list[id] = 2
            picks[2] -= 1
            continue

    pick_index = 0
    hp = 5
    for mineral in minerals:
        if (hp == 0):
            pick_index += 1
            hp = 5

        while (pick_index < len(pick_order_list)):
            if (pick_order_list[pick_index] != -1):
                break
            pick_index += 1
            
        if (pick_index >= len(pick_order_list)):
            break
        
        pick = pick_order_list[pick_index]
        answer += fatigue_info[pick][mineral_index_dict[mineral]]
        hp -= 1
        
    return answer