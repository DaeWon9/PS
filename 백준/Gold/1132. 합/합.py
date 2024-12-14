import sys
from collections import defaultdict
input = sys.stdin.readline

# 특정 알파벳이 얼만큼 더해지는지 계산한다.
# 위에서 구한 계산결과를 내림차순으로 정렬한다.
# 9~0 까지 배치해준다.
# 입력으로 들어온 숫자중 맨앞이 0이 되는지 확인해준다.
# 0이 된다면 땡겨준다.

value_dict = defaultdict(lambda: [0, False])
result_list = []

N = int(input())
for _ in range(N):
    data = input().rstrip()
    data_len = len(data)

    for i in range(data_len):
        key = data[i]
        zero = data_len - i - 1
        value = '1' + ('0' * zero)
        value = int(value)
        value_dict[key][0] += value

        if (i == 0):
            value_dict[key][1] = True

n = 9
tmp_index = 0
last_index = 0
flag = False

sorted_list = sorted(value_dict.items(), key= lambda x: value_dict[x[0][0]], reverse=True)
for key, value in sorted_list:
    if (not value[1]):
        tmp_index = 9 - n
    
    if (n == 0 and value[1]):
        flag = True
        last_index = 9 - n
    
    result_list.append([key, n])
    n -= 1

if (flag):
    result_list[last_index][1] = 1
    result_list[tmp_index][1] = 0
    for i in range(tmp_index + 1, last_index):
        result_list[i][1] += 1

answer = 0
for key, value in result_list:
    answer += value_dict[key][0] * value
print(answer)