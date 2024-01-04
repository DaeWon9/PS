import sys
from collections import defaultdict

n = int(sys.stdin.readline())
num_list = []
num_bindo_dict = defaultdict(int)
hit_dict = defaultdict(int)

for _ in range(n):
    input_num = int(sys.stdin.readline())
    num_list.append(input_num)
    num_bindo_dict[input_num] += 1

for i in range(n):
    for k in range(1, int(num_list[i] ** 0.5) + 1):
        if num_list[i] % k == 0:
            if num_list[i] // k != k:
                hit_dict[i] += num_bindo_dict[k] + num_bindo_dict[num_list[i] // k]
            else:
                hit_dict[i] += num_bindo_dict[k]

    print(hit_dict[i] - 1)
