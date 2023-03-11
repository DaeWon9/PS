import sys

switch_n = int(sys.stdin.readline())
switch_status_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

student_n = int(sys.stdin.readline())
student_info = []

for i in range(student_n):
    student_info.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in range(student_n):
    target_index = student_info[i][1] - 1
    if (student_info[i][0] == 1): # 남자
        for j in range(target_index, switch_n, student_info[i][1]):
            if (switch_status_list[j] == 1):
                switch_status_list[j] = 0
            else:
                switch_status_list[j] = 1
    else: # 여자
        left_index = target_index
        right_index = target_index
        checked_left_index = target_index
        checked_right_index = target_index

        if(target_index == 0 or target_index == switch_n-1):
            for j in range(checked_left_index, checked_right_index + 1):
                if (switch_status_list[j] == 1):
                    switch_status_list[j] = 0
                else:
                    switch_status_list[j] = 1
        else:
            while True:
                left_index = left_index - 1
                right_index = right_index + 1
                
                if(left_index < 0 or right_index > switch_n-1):
                    break

                if (switch_status_list[left_index] == switch_status_list[right_index]):
                    checked_left_index = left_index
                    checked_right_index = right_index
                else:
                    break

            for j in range(checked_left_index, checked_right_index + 1):
                if (switch_status_list[j] == 1):
                    switch_status_list[j] = 0
                else:
                    switch_status_list[j] = 1
                
count = 0
for item in switch_status_list:
    print(item, end=" ")
    count += 1
    if (count % 20 == 0):
        print("")
