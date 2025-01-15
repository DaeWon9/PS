import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = -2147483648
table = []
summed_area_table = [[0] * (M + 1) for _ in range(N + 1)]

for _ in range(N):
    table.append(list(map(int, input().split())))

for r in range(1, N + 1):
    for c in range(1, M + 1):
        summed_area_table[r][c] = (
            table[r - 1][c - 1] +
            summed_area_table[r - 1][c] +
            summed_area_table[r][c - 1] -
            summed_area_table[r - 1][c - 1]
        )

for start_row in range(1, N + 1):
    for start_col in range(1, M + 1):
        for end_row in range(start_row, N + 1):
            for end_col in range(start_col, M + 1):
                result_sum = (
                    summed_area_table[end_row][end_col]
                    - summed_area_table[start_row - 1][end_col]
                    - summed_area_table[end_row][start_col - 1]
                    + summed_area_table[start_row - 1][start_col - 1]
                )
                answer = max(answer, result_sum)

print(answer)
