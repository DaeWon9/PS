import sys

villiage_info_list = []
whole_people_count = 0

n = int(sys.stdin.readline())

for _ in range(n):
    n_viliage, people = map(int, sys.stdin.readline().split())
    villiage_info_list.append((n_viliage, people))
    whole_people_count += people

villiage_info_list.sort() 
half_people_count = whole_people_count / 2
value = 0
answer = 0

for village_info in villiage_info_list:
    value += village_info[1]
    
    if (value >= half_people_count):
        answer = village_info[0]
        break

print(answer)