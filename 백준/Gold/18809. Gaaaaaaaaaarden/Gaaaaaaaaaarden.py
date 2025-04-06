import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, M, G, R = map(int, input().split())
board = []
candidates = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if (row[j] == 2):
            candidates.append((i, j))

answer = 0

def bfs(g_pos, r_pos):
    q = deque()
    visited = [[[-1, ''] for _ in range(M)] for _ in range(N)]  # 시간, 색상
    flower = 0

    for r, c in g_pos:
        q.append((r, c, 0, 'G'))
        visited[r][c] = [0, 'G']
    for r, c in r_pos:
        q.append((r, c, 0, 'R'))
        visited[r][c] = [0, 'R']

    while q:
        r, c, t, color = q.popleft()
        if (visited[r][c][1] == 'F'):
            continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if (0 <= nr < N and 0 <= nc < M and board[nr][nc] != 0):
                vt, vc = visited[nr][nc]

                if (vc == ''):
                    visited[nr][nc] = [t + 1, color]
                    q.append((nr, nc, t + 1, color))
                elif (vt == t + 1 and vc != color and vc != 'F'):
                    flower += 1
                    visited[nr][nc][1] = 'F'

    return flower

for comb in combinations(candidates, G + R):
    for g_pos in combinations(comb, G):
        g_set = set(g_pos)
        r_pos = [pos for pos in comb if pos not in g_set]
        flower = bfs(g_pos, r_pos)
        answer = max(answer, flower)

print(answer)
