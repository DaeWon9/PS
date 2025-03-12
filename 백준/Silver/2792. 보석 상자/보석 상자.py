import sys
input = sys.stdin.readline

# target count를 잡고
# 이분탐색으로 값을 조절하며 해당 count로 보석들을 나눌 수 있는지 체크

N, M = map(int, input().split())
jewels = []
max_count = 0
answer = 0

for _ in range(M):
    input_data = int(input())
    max_count = max(max_count, input_data)
    jewels.append(input_data)


left = 1
right = max_count

while (left <= right):
    mid = (left + right) // 2
    temp_count = 0

    for jewel in jewels:
        temp_count += (jewel // mid)
        if (jewel % mid != 0):
            temp_count += 1

    if (temp_count <= N):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)