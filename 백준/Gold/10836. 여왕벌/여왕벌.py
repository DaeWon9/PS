import sys
input = sys.stdin.readline

M, N = map(int, input().split())
edge_count = 2 * M - 1
arr = [0] * edge_count

for _ in range(N):
    zero_c, one_c, two_c = map(int, input().split())
    idx = zero_c

    if (zero_c < edge_count):
        arr[zero_c] += 1
    if (zero_c + one_c < edge_count):
        arr[zero_c + one_c] += 1

summed_table = [0] * edge_count
summed_table[0] = arr[0]

for i in range(1, edge_count):
    summed_table[i] = summed_table[i-1] + arr[i]

for r in range(M):
    for c in range(M):
        if (c == 0):
            print(summed_table[M-r-1] + 1, end=" ")
        else:
            print(summed_table[M+c-1] + 1, end=" ")
    print()