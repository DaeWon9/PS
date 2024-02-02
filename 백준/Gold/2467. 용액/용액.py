import sys
input = sys.stdin.readline

def solution():
    left = 0
    right = n - 1

    min_diff = 2000000000
    ans_left_value = 0
    ans_right_value = 0
    
    while left < right:
        diff = value_list[left] + value_list[right]

        if (min_diff > abs(diff)):
            min_diff = abs(diff)
            ans_left_value = value_list[left]
            ans_right_value = value_list[right]

            if (min_diff == 0):
                print(ans_left_value, ans_right_value)
                return
        
        if diff < 0:
            left += 1
        else:
            right -= 1

    print(ans_left_value, ans_right_value)
    return

n = int(input())
value_list = list(map(int, input().split()))

solution()