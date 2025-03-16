import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

left = 0
right = 1_000_000_000
answer = 0

while (left <= right):
    mid = (left + right) // 2

    cur_pos = arr[0]
    count = 1

    for i in range(1, N):
        if (arr[i] - mid >= cur_pos):
            count += 1
            cur_pos = arr[i]

    if (count >= C):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)