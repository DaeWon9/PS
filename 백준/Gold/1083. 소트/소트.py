import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = int(input())

# S만큼 교환했을 때, 사전 순으로 가장 뒷서려면 -> 맨앞에 가장 큰 수
# 앞으로 옮길 수 있는 가장 큰 수를 찾고
# 타고타고 올라오면서 바꾼다.

for i in range(N):
    max_num = A[i]
    max_idx = i

    max_range = min(N, i+S+1)
    for j in range(i+1, max_range):
        if (max_num < A[j]):
            max_num = A[j]
            max_idx = j
    
    for j in range(max_idx, i, -1):
        A[j], A[j-1] = A[j-1], A[j]
    
    swap_count = max_idx - i
    S -= swap_count

    if (S < 1):
        break

print(*A)