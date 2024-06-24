import sys
input = sys.stdin.readline

num_list = list(map(int, input().split()))
answer = min(num_list)

while(True):
    div_count = 0
    for num in num_list:
        if (answer % num == 0):
            div_count += 1
    
    if (div_count > 2):
        break

    answer += 1

print(answer)