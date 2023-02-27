import sys

N = int(input())

time_list = []
for i in range(N):
    time_list.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

time_list = sorted(time_list, key = lambda x:(x[1],x[0]))
finish_time = time_list[0][1]
count = 1

for index in range(1, N):
    if (time_list[index][0] >= finish_time):
        count += 1
        finish_time = time_list[index][1]

print(count)