import sys

N = int(input())
price_list = []
sum = 0

for _ in range(N):
    price_list.append(int(sys.stdin.readline().rstrip()))

price_list.sort(reverse=True)

for i in range(N // 3):
    sum = sum + price_list[i * 3] + price_list[i * 3 + 1]

for i in range(1, N % 3 + 1):
    sum = sum + price_list[-i]

print(sum)