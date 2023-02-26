import sys

N = int(input())

whole_length = 0
price_sum = 0

length_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
whole_length = sum(length_list)

price_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
price_list = price_list[:-1]

min_price = min(price_list)
remain_length = whole_length

for i in range(N):
    if (price_list[i] == min_price):
        price_sum = price_sum + (min_price * remain_length)
        break
    else:
        price_sum = price_sum + (price_list[i] * length_list[i])
        remain_length = remain_length - length_list[i]

print(price_sum)