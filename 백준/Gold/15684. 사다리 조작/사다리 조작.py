import sys
input = sys.stdin.readline

def is_answer():
    for start_col in range(1, N + 1):
        col = start_col
        for row in range(1, H + 1):
            if ladder[row][col] == 1:
                col += 1
            elif ladder[row][col - 1] == 1:
                col -= 1
        if col != start_col:
            return False
    return True

def backtrack(count, row, col):
    global found
    if found:  # 이미 답을 찾았으면 중단
        return
    if count == target_count:
        if is_answer():
            found = True
        return

    for r in range(row, H + 1):
        for c in range(1, N):
            if ladder[r][c] == 0 and ladder[r][c - 1] == 0 and ladder[r][c + 1] == 0:
                ladder[r][c] = 1
                backtrack(count + 1, r, c + 2)  # 다음 열로 이동
                ladder[r][c] = 0  # 복구

N, M, H = map(int, input().split())
ladder = [[0] * (N + 1) for _ in range(H + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1

found = False
for target_count in range(4):  # 사다리 추가 개수 0~3
    backtrack(0, 1, 1)
    if found:
        print(target_count)
        exit(0)

print(-1)
