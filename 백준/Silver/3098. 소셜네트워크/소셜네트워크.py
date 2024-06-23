import sys
from collections import defaultdict
input = sys.stdin.readline

def is_all_people_connected():
    if (False in connect_status):
        return False
    return True

N, M = map(int, input().split())

friend_info_dict = defaultdict(set)
connect_status = [False] * (N + 1)
connect_status[0] = True
answer = []

for i in range(1, N + 1):
    friend_info_dict[i].add(i)

day = 0

for _ in range(M):
    A, B = map(int, input().split())
    friend_info_dict[A].add(B)
    friend_info_dict[B].add(A)

    if (len(friend_info_dict[A]) == N):
        connect_status[A] = True
            
    if (len(friend_info_dict[B]) == N):
        connect_status[B] = True

while (True):
    if (is_all_people_connected()):
        break

    added_pair_info = set()

    for person in range(1, N + 1):
        if (connect_status[person]):
            continue

        for connected_friend in friend_info_dict[person]:
            for new_friend in friend_info_dict[connected_friend]:
                if (new_friend in friend_info_dict[person]):
                    continue
                
                if ((new_friend, person) not in added_pair_info
                    and (person, new_friend) not in added_pair_info):
                    added_pair_info.add((person, new_friend))
    
    for p1, p2 in added_pair_info:
        friend_info_dict[p1].add(p2)
        friend_info_dict[p2].add(p1)

        if (len(friend_info_dict[p1]) == N):
            connect_status[p1] = True
        
        if (len(friend_info_dict[p2]) == N):
            connect_status[p2] = True

    answer.append(len(added_pair_info))
    day += 1

print(day)
for count in answer:
    print(count)