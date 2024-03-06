import sys
input = sys.stdin.readline

N, warrior_atk_power = map(int, input().split())

room_info = []

max_warrior_atk_power = warrior_atk_power

for _ in range(N):
    case, atk_power, hp = (list(map(int, input().split())))
    if (case == 2):
        max_warrior_atk_power += atk_power

    room_info.append((case, atk_power, hp)) 

max_hp = 1

for i in range(len(room_info) - 1, -1, -1):
    if (room_info[i][0] == 1):
        if (room_info[i][2] % max_warrior_atk_power == 0):
            max_hp = (room_info[i][2] // max_warrior_atk_power - 1) * room_info[i][1] + 1
        else:
            max_hp = (room_info[i][2] // max_warrior_atk_power) * room_info[i][1] + 1
        break

cur_hp = max_hp

for case, atk_power, hp in room_info:
    if (case == 1): # monster
        if (hp % warrior_atk_power == 0):
            cur_hp -= ((hp // warrior_atk_power - 1) * atk_power)
        else:
            cur_hp -= ((hp // warrior_atk_power) * atk_power)
        
        if (cur_hp < 1): 
            max_hp += (1 - cur_hp)
            cur_hp = 1
    else: # potion
        warrior_atk_power += atk_power
        cur_hp += hp

        if (cur_hp > max_hp):
            cur_hp = max_hp

print(max_hp)