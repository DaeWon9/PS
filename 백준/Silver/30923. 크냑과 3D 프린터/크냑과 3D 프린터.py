import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
diff_sum = 0
prev_height = H[0]
default_area = H[0] + H[-1] + 2 * (N + sum(H))

for i in range(1, N):
    diff_sum += abs(prev_height - H[i])
    prev_height = H[i]

print(default_area + diff_sum)