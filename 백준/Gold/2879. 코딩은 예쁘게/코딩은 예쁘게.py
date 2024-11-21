import sys
input = sys.stdin.readline

N = int(input())
cur = list(map(int, input().split()))
goal = list(map(int, input().split()))
gap = []
for i in range(N):
    gap.append(goal[i] - cur[i])

answer = 0
flag = True

while flag:
    flag = False
    i = 0
    while i < N:
        if (gap[i] == 0):
            i += 1
            continue
        flag = True
        min_v = gap[i]
        for j in range(i + 1, N + 1):
            if (j == N or gap[i] * gap[j] <= 0):
                answer += abs(min_v)
                for k in range(i, j):
                    gap[k] -= min_v
                i = j - 1
                break
            if (abs(gap[j]) < abs(min_v)):
                min_v = gap[j]
        i += 1

print(answer)
