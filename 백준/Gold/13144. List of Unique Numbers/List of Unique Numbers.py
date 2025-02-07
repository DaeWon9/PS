import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = 0
answer = 0
num_set = set()

while (start <= end and start < n and end < n):
    if (arr[end] in num_set):
        num_set.remove(arr[start])
        start += 1
    else:
        num_set.add(arr[end])
        end += 1
        answer += len(num_set)

print(answer)