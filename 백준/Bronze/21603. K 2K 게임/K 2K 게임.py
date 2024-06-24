import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K2 = K * 2
K2 = K2 % 10
K = K % 10

answer = []

for i in range(1, N + 1):
    if (i % 10 == K or i % 10 == K2):
        continue
    answer.append(i)

print(len(answer))
for ans in answer:
    print(ans, end=' ')