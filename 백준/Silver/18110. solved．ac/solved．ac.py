import sys

def round45(num):
    return int(num + 0.5)

N = int(sys.stdin.readline())
level_list = []
except_count = round45(N * 0.15)
sum = 0

if (N == 0):
    print(0)
    exit(0)

for i in range(N):
    level_list.append(int(sys.stdin.readline()))

level_list.sort()

for i in range(except_count, len(level_list) - except_count):
    sum += level_list[i]

print(round45(sum / (N - except_count * 2)))