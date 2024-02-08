import sys
input = sys.stdin.readline

def solution(num_list):
    sorted_list = []
    answer = []

    for index, num in enumerate(num_list):
        if (index == 0):
            sorted_list.append(num)
            answer.append(num)
            continue
        
        left_index = 0
        right_index = index - 1
        target_index = 0
 
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if (sorted_list[mid_index] < num):
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1
            
            if (left_index == mid_index or mid_index == right_index):
                if (sorted_list[mid_index] < num):
                    target_index = mid_index + 1
                else:
                    target_index = mid_index
                break

        if (target_index == -1):
            sorted_list.insert(0, num)
        else:
            sorted_list.insert(target_index, num)

        if ((index + 1) % 2 == 1):
            answer.append(sorted_list[index // 2])

    return answer

T = int(input())

for _ in range(T):
    M = int(input())

    num_list = list(map(int, input().split()))
    for i in range(M // 10):
        plus_list = list(map(int, input().split()))
        for num in plus_list:
            num_list.append(num)

    result = solution(num_list)
    print(len(result))
    for index, num in enumerate(result):
        if (index % 10 == 9):
            print(num)
        else:
            print(num, end=' ')
