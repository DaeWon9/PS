import sys
input = sys.stdin.readline

N = int(input())
info_list = []

for _ in range(N):
    s, e = map(int, input().split())
    info_list.append((s, 1))  # 시작 +1
    info_list.append((e, -1)) # 종료 -1
info_list.sort()

max_count = 0
current_count = 0
max_range = [0, 0]
open_flag = False

for time, case in info_list:
    prev_count = current_count
    current_count += case

    if (current_count > max_count): # 최대 구간 시작
        change_count = 0
        max_count = current_count
        max_range = [time, time]
        open_flag = True
    elif (current_count == max_count): # same
        if (prev_count == max_count - 1 and time == max_range[1] and open_flag):
            max_range[1] = time
        else:
            open_flag = False
    else: # 현재가 더 작음
        if (prev_count == max_count and open_flag): # 연장
            max_range[1] = time
        else:
            open_flag = False

print(max_count)
print(*max_range)