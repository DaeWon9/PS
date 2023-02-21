N = int(input())

weight_list = []
max_weight_list = []

for _ in range(N):
    weight_list.append(int(input()))

weight_list = sorted(weight_list, reverse=True)

for index in range(N):
    max_weight_list.append(weight_list[index] * (index + 1))

print(max(max_weight_list))