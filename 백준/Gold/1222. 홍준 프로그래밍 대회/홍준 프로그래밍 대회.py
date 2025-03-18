import sys
input = sys.stdin.readline

MAX_RANGE = 2_000_001
n = int(input())
divisor = [0] * MAX_RANGE

for data in list(map(int, input().split())):
    divisor[data] += 1

answer = 0

for i in range(1, MAX_RANGE):
    cnt = 0
    for j in range(i, MAX_RANGE, i):
        cnt += divisor[j]
    
    if (cnt >= 2):
        answer = max(answer, cnt * i)

print(answer)