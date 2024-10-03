import sys
input = sys.stdin.readline

# N: 행(row), M: 열(col)
N, M = map(int, input().split())
summed_area_table = [[0 for _ in range(M)] for _ in range(N)]
table = []
answer = 0

# 원본 테이블 입력 받기
for _ in range(N):
    table.append(list(map(int, list(input().rstrip()))))

# 누적합 테이블(summed_area_table) 생성
summed_area_table[0][0] = table[0][0]

# 첫 번째 행 누적합 계산
for col in range(1, M):
    summed_area_table[0][col] = summed_area_table[0][col - 1] + table[0][col]

# 첫 번째 열 누적합 계산
for row in range(1, N):
    summed_area_table[row][0] = summed_area_table[row - 1][0] + table[row][0]

# 나머지 셀들에 대해 누적합 계산
for row in range(1, N):
    for col in range(1, M):
        summed_area_table[row][col] = (summed_area_table[row - 1][col]
                                        + summed_area_table[row][col - 1]
                                        - summed_area_table[row - 1][col - 1]
                                        + table[row][col])

# 직사각형의 합을 구하는 함수
def sum_rectangle(x1, y1, x2, y2):
    # 경계값 체크
    total = summed_area_table[x2][y2]
    if (x1 > 0):
        total -= summed_area_table[x1 - 1][y2]
    if (y1 > 0):
        total -= summed_area_table[x2][y1 - 1]
    if (x1 > 0 and y1 > 0):
        total += summed_area_table[x1 - 1][y1 - 1]
    return total

# 세로로 나누는 경우
for i in range(0, M - 2):
    for j in range(i + 1, M - 1):
        r1 = sum_rectangle(0, 0, N - 1, i)
        r2 = sum_rectangle(0, i + 1, N - 1, j)
        r3 = sum_rectangle(0, j + 1, N - 1, M - 1)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

# 가로로 나누는 경우
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        r1 = sum_rectangle(0, 0, i, M - 1)
        r2 = sum_rectangle(i + 1, 0, j, M - 1)
        r3 = sum_rectangle(j + 1, 0, N - 1, M - 1)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

# 세로 + 가로 혼합 분할 (세로 먼저 나누고 가로로 나누는 경우)
for i in range(0, M - 1):
    for j in range(0, N - 1):
        r1 = sum_rectangle(0, 0, N - 1, i)
        r2 = sum_rectangle(0, i + 1, j, M - 1)
        r3 = sum_rectangle(j + 1, i + 1, N - 1, M - 1)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

# 가로 + 세로 혼합 분할 (가로 먼저 나누고 세로로 나누는 경우)
for i in range(0, N - 1):
    for j in range(0, M - 1):
        r1 = sum_rectangle(0, 0, i, j)
        r2 = sum_rectangle(i + 1, 0, N - 1, j)
        r3 = sum_rectangle(0, j + 1, N - 1, M - 1)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

# 혼합 분할 (가로 세로 혼합, 나머지 경우)
for i in range(0, N - 1):
    for j in range(0, M - 1):
        r1 = sum_rectangle(0, 0, i, M - 1)
        r2 = sum_rectangle(i + 1, 0, N - 1, j)
        r3 = sum_rectangle(i + 1, j + 1, N - 1, M - 1)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

for i in range(0, N - 1):
    for j in range(0, M - 1):
        r1 = sum_rectangle(0, 0, i, j)
        r2 = sum_rectangle(0, j + 1, i, M - 1)
        r3 = sum_rectangle(i + 1, 0, N - 1, M - 1)
        if answer < r1 * r2 * r3:
            answer = r1 * r2 * r3

# 결과 출력
print(answer)