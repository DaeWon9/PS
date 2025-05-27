import sys
input = sys.stdin.readline

n = int(input())
arr = set(list(map(int, input().split())))
x = int(input())

answer = 0

for item in arr:
    target = x - item
    if (target in arr):
        answer += 1

print(answer // 2)