import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K = K % 10

answer = []

for i in range(1, N + 1):
    if (i % 10 == K or i % 10 == 2 * K):
        continue
    answer.append(i)

print(len(answer))
for ans in answer:
    print(ans, end=' ')