import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = N-1
min_sum = 2000000001
answer = []

while (start < end):
    sum = arr[start] + arr[end]
    abs_sum = abs(sum)

    if (min_sum > abs_sum):
        min_sum = abs_sum
        answer = [arr[start], arr[end]]

    if (sum < 0):
        start += 1
    else:
        end -= 1

print(*answer)
    
