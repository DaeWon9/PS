import sys
input = sys.stdin.readline

M, N = map(int, input().split())

table = [[1 for _ in range(M)] for _ in range(M)]
edge_count = 2 * M - 1
arr = [0] * edge_count

for _ in range(N):
    zero_c, one_c, two_c = map(int, input().split())
    idx = zero_c

    arr[zero_c] += 1
    if (zero_c + one_c < edge_count):
        arr[zero_c + one_c] += 1

summed_table = [0] * edge_count
summed_table[0] = arr[0]

for i in range(1, 2*M-1):
    summed_table[i] = summed_table[i-1] + arr[i]

dr = [-1, 0]
dc = [0, 1]
i = 0

row = M
col = 0

for num in summed_table:
    row += dr[i]
    col += dc[i]

    if (row == -1):
        row = 0
        col = 1
        i = 1

    table[row][col] += num

for r in range(1, M):
    for c in range(1, M):
        table[r][c] = max(table[r-1][c-1], table[r-1][c], table[r][c-1])

for t in table:
    print(*t)