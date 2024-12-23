import sys
input = sys.stdin.readline

N, A, D = map(int, input().split())
H = list(map(int, input().split()))
target = A
answer = 0
for i in range(N):
    if (H[i] == target):
        answer += 1
        target += D

print(answer)