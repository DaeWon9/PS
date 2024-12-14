import sys
from collections import defaultdict
input = sys.stdin.readline

# 특정 알파벳이 얼만큼 더해지는지 계산한다.
# 위에서 구한 계산결과를 내림차순으로 정렬한다.
# 9~0 까지 배치해준다.

value_dict = defaultdict(int)
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
        value_dict[key] += value

n = 9
sorted_list = sorted(value_dict.items(), key= lambda x: value_dict[x[0]], reverse=True)
for key, value in sorted_list:
    result_list.append([key, n])
    n -= 1

answer = 0
for key, value in result_list:
    answer += value_dict[key] * value
print(answer)