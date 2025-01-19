import sys
input = sys.stdin.readline

n = int(input())
result_sum = 0
result_range = []

for _ in range(n):
    L = int(input())
    arr = list(map(int, input().split()))

    max_sum = arr[0]
    l, r = 0, 0
    ml, mr = 0, 0

    for i in range(1, L):
        if (arr[i] < arr[i-1] + arr[i]): # 누적합이 더 클 때
            arr[i] += arr[i-1]
            r = i
        else: # 손해인 경우, 리셋
            l = i
            r = i
        
        if (max_sum < arr[i]): # 최대치 갱신
            max_sum = arr[i]
            ml = l
            mr = r
        elif (max_sum == arr[i]): # 최대치가 같을 경우, 개수가 최소
            prev_range = mr - ml
            new_range = r - l

            if (prev_range > new_range):
                mr = r
                ml = l
    
    result_sum += max_sum
    result_range.append((ml + 1, mr + 1))

print(result_sum)
for result in result_range:
    print(*result)