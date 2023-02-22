import sys

N = int(input())

amount_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

amount_list.sort(reverse=True)

sum = amount_list[0]

for i in range(1, N):
    sum = sum + amount_list[i] / 2

print(sum)