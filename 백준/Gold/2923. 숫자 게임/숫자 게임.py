import sys
input = sys.stdin.readline

MAX = 101
A = [0] * MAX
B = [0] * MAX

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    A[a] += 1
    B[b] += 1

    temp_A = A[:]
    temp_B = B[:]

    result = 0
    a_idx = 100
    b_idx = 1

    while (a_idx >= 1 and b_idx < MAX):
        while (a_idx >= 1 and temp_A[a_idx] == 0):
            a_idx -= 1
        while (b_idx < MAX and temp_B[b_idx] == 0):
            b_idx += 1

        if (a_idx == 0 or b_idx == MAX):
            break

        result = max(result, a_idx + b_idx)

        if (temp_A[a_idx] > temp_B[b_idx]):
            temp_A[a_idx] -= temp_B[b_idx]
            temp_B[b_idx] = 0
        else:
            temp_B[b_idx] -= temp_A[a_idx]
            temp_A[a_idx] = 0

    print(result)
