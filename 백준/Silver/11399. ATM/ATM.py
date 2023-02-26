N = int(input())
P = list(map(int, input().split(" ")))

time_sum = 0

P = sorted(P)

for i in range(N):
    time_sum = time_sum + (P[i] * (N - i))

print(time_sum)