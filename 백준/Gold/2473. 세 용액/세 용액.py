import sys
input = sys.stdin.readline

n = int(input())
value_list = list(map(int, input().split()))
value_list.sort()
min_sum = 4000000000
answer = [value_list[0], value_list[1], value_list[2]]

for pivot_index in range(n - 2):
    pviot = value_list[pivot_index]

    left_index = pivot_index + 1
    right_index = n - 1

    while (left_index < right_index):
        temp_sum = pviot + value_list[left_index] + value_list[right_index]

        if abs(temp_sum) < min_sum: 
            answer = [pviot, value_list[left_index], value_list[right_index]]
            min_sum = abs(temp_sum)

        if temp_sum == 0:
            print(answer[0], answer[1], answer[2])
            exit(0)
        elif temp_sum < 0:
            left_index += 1
        else:
            right_index -= 1

print(answer[0], answer[1], answer[2])