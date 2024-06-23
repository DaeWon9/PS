import sys
input = sys.stdin.readline

init = input()
N = int(input())

in_home_people_list = set()
seen_people_list = set()
for _ in range(N):
    in_home_people_list.add(input().rstrip())

M = int(input())

for _ in range(M):
    seen_people_list.add(input().rstrip())

if("dongho" in in_home_people_list):
    print("dongho")
    exit(0)

sub_set = in_home_people_list - seen_people_list
if (len(sub_set) == 1):
    print(list(sub_set)[0])
    exit(0)

if ("bumin" in sub_set):
    print("bumin")
    exit(0)

if ("cake" in sub_set):
    print("cake")
    exit(0)

if ("lawyer" in sub_set):
    print("lawyer")
    exit(0)

if (sub_set):
    sub_sorted_list = list(sub_set)
    sub_sorted_list.sort()
    print(sub_sorted_list[0])
else:
    print("swi")
