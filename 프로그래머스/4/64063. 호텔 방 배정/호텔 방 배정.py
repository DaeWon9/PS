from collections import defaultdict

class Room:
    def __init__(self, value = -1):
        self.value = value
        self.next = None
        self.isSelected = False

def solution(k, room_number):
    answer = []
    room_dict = defaultdict(Room)
    
    
    for number in room_number:
        if (room_dict[number].isSelected): # 사용자가 원하는 방이 선택되어있는경우
            #next 계속 이동
            visited_index_list = []
            next_room = room_dict[number].next
            next_index = next_room.value
            visited_index_list.append(next_index)
            
            while(True):
                if (next_room.isSelected == True):
                    next_room = next_room.next
                    next_index = next_room.value
                    visited_index_list.append(next_index)
                else:
                    break
            
            
            next_room.isSelected = True
            next_room.value = next_index
            next_room.next = room_dict[next_index + 1]
            next_room.next.value = next_index + 1
            answer.append(next_index)
            
            for visited_index in visited_index_list:
                room_dict[visited_index].next = room_dict[next_index + 1]
    
        
        else: # 사용자가 원하는 방이 선택되어있지 않은 경우
            room_dict[number].isSelected = True
            room_dict[number].value = number
            room_dict[number].next = room_dict[number+1]
            room_dict[number].next.value = number + 1
            answer.append(number)

    return answer