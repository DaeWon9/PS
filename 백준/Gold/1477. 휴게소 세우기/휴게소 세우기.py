import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
if (N > 0):
    arr = [0] + list(map(int, input().split())) + [L]
else:
    arr = [0, L]

arr.sort()

left = 1
right = L - 1
answer = 0

while (left <= right):
    mid = (left + right) // 2
    temp_count = 0
    last_pos = 0

    for pos in arr:
        while (pos - last_pos > mid):
            temp_count += 1
            last_pos += mid

        last_pos = pos
    
    if (temp_count <= M):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
        
print(answer)
