n = int(input())

count_dict = dict()

count_dict[1] = 1
count_dict[2] = 3

for index in range(3, n+1):
    count_dict[index] = count_dict[index-1] + count_dict[index-2] * 2

print(count_dict[n] % 10007)