import sys
input = sys.stdin.readline

def dfs(index, count, pos_list, visited_diag1, visited_diag2):
    global max_count
    if (index == len(pos_list)):
        max_count = max(max_count, count)
        return

    r, c = pos_list[index]
    d1 = r + c
    d2 = r - c + N - 1

    if (not visited_diag1[d1] and not visited_diag2[d2]):
        visited_diag1[d1] = visited_diag2[d2] = True
        dfs(index + 1, count + 1, pos_list, visited_diag1, visited_diag2)
        visited_diag1[d1] = visited_diag2[d2] = False

    dfs(index + 1, count, pos_list, visited_diag1, visited_diag2)


N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

black_pos = []
white_pos = []

for r in range(N):
    for c in range(N):
        if (board[r][c] == 1):
            if (r + c) % 2 == 0:
                black_pos.append((r, c))
            else:
                white_pos.append((r, c))

max_count = 0
dfs(0, 0, black_pos, [False]*(2*N), [False]*(2*N))
black_max = max_count

max_count = 0
dfs(0, 0, white_pos, [False]*(2*N), [False]*(2*N))
white_max = max_count

print(black_max + white_max)
