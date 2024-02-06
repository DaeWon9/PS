import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

start_index = 0
end_index = 0
sum = num_list[start_index]
answer = 100001

while True:
    if sum < S:
        end_index += 1
        if end_index == N: 
            break
        sum += num_list[end_index]
    else:
        sum -= num_list[start_index]
        answer = min(answer, end_index - start_index + 1)
        start_index += 1
        
if answer == 100001:
    print(0)
else:
    print(answer)