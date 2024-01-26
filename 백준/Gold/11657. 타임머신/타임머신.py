import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []

for _ in range(m):
    edges.append(list(map(int, input().split())))

time_list = [2147483647] * (n + 1)
time_list[1] = 0

is_has_minus_cycle = False

for count in range(n):
    for start, end, time in edges:
        if (time_list[start] != 2147483647 and time_list[end] > time_list[start] + time):
            time_list[end] = time_list[start] + time

            if (count == n-1):
                is_has_minus_cycle = True

if(is_has_minus_cycle):
    print(-1)
else:
    for i in range(2, n+1):
        if (time_list[i] == 2147483647):
            print(-1)
        else:
            print(time_list[i])
