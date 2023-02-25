import sys

N = int(input())

tip = 0
tip_list = []

for _ in range(N):
    tip_list.append(int(sys.stdin.readline().rstrip()))

tip_list.sort(reverse=True)

for index in range(N):
    calculated_tip = tip_list[index] - index
    if (calculated_tip > 0):
        tip = tip + calculated_tip

print(tip)