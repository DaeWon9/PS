import sys

n = int(sys.stdin.readline())

array = []

for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

array.append(array[0])

x = 0
y = 0

for i in range(n):
    x += array[i][0] * array[i + 1][1]
    y += array[i][1] * array[i + 1][0]

answer = round((x - y) / 2, 1)

print(abs(answer))