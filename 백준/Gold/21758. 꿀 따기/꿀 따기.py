import sys
input = sys.stdin.readline

def get_area_sum(left, right):
    if (left > right):
        left, right = right, left

    if (left == 0):
        return summed_arr[right]
    
    return summed_arr[right] - summed_arr[left-1]
    
# 제한시간 1초 -> N이 10만이면 O(N^2)으로 풀면 시간초과
# 최대가 되려면, 배열의 전체가 포함되어야함.
# 벌통이 제일 왼쪽 Or 제일 오른쪽 or 중앙 어딘가
N = int(input()) # 3 <= N <= 100_000
arr = list(map(int, input().split()))
summed_arr = [0 for _ in range(N)]
summed_arr[0] = arr[0]
answer = 0

for i in range(1, N):
    summed_arr[i] = summed_arr[i-1] + arr[i]

# case1, 벌통이 제일 왼쪽, 벌한마리 오른쪽 끝
case_1 = summed_arr[-1] - arr[-1]
for i in range(1, N-1):
    answer = max(answer, case_1 + get_area_sum(0, i) - arr[i] - arr[i])

# case2, 벌통이 제일 오른쪽, 벌한마리 왼쪽 끝
case_2 = summed_arr[-1] - arr[0]
for i in range(1, N-1):
    answer = max(answer, case_2 + get_area_sum(i, N-1) - arr[i] - arr[i])

# case3, 양쪽 끝에 벌, 중앙 어딘가에 벌통
for i in range(1, N-1):
    answer = max(answer, get_area_sum(1, i) + get_area_sum(i, N-2))

print(answer)