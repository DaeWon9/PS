import sys

# 특정 구간 내에 두 수의 합이 특정 값이 되는걸 판별
# -> 투포인터

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

answer = 0

for target_index in range(n):
    target_sum = num_list[target_index]

    start = 0
    end = n - 1
 
    while (start < end):
        sum = num_list[start] + num_list[end]
        if (sum == target_sum):
            if (start == target_index):
                start += 1    
                continue    
            if (end == target_index):
                end -= 1
                continue
            
            answer += 1
            break
        
        if (sum > target_sum):
            end -= 1
        else:
            start += 1

print(answer)