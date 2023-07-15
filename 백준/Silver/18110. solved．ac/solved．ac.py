import sys

N = int(sys.stdin.readline())
level_list = []
except_count = int((N * 0.15) + 0.5)
sum = 0

if (N == 0):
    print(0)
    exit(0)

for i in range(N):
    level_list.append(int(sys.stdin.readline()))

level_list.sort()

for i in range(except_count, len(level_list) - except_count):
    sum += level_list[i]

print(int((sum / (N - except_count * 2)) + 0.5))