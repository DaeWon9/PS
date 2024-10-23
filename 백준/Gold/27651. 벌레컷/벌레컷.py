import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

summed_A = [0] * N
summed_A[0] = A[0]

for i in range(1, N):
    summed_A[i] = summed_A[i - 1] + A[i]

answer = 0

for i in range(N - 1, 1, -1):
    left = 1
    right = i - 1
    max_idx = 0

    while left <= right:
        mid = (left + right) // 2

        head = summed_A[mid - 1]  # 머리: A[0] ~ A[mid-1]
        chest = summed_A[i - 1] - summed_A[mid - 1]  # 가슴: A[mid] ~ A[i-1]
        belly = summed_A[N - 1] - summed_A[i - 1]  # 배: A[i] ~ A[N-1]

        if (head < belly < chest):
            max_idx = max(max_idx, mid)
            left = mid + 1
        else:
            right = mid - 1

    answer += max_idx

print(answer)
