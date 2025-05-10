import sys
input = sys.stdin.readline

def convert_pos(idx):
    return idx // M, idx % M

def is_movable(r, c):
    return 0 <= r < N and 0 <= c < M

# 부메랑 4방향 (중심, 모서리1, 모서리2)
boomerangs = [
    ((0, 0), (1, 0), (0, 1)),    # 아래, 오른쪽
    ((0, 0), (0, 1), (-1, 0)),   # 오른쪽, 위
    ((0, 0), (-1, 0), (0, -1)),  # 위, 왼쪽
    ((0, 0), (0, -1), (1, 0)),   # 왼쪽, 아래
]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0

def solve(idx, temp):
    global answer

    if (idx == N*M): # last
        answer = max(answer, temp)
        return
    
    r, c = convert_pos(idx)

    if (visited[r][c]):
        solve(idx+1, temp)
        return
    
    for boomerang in boomerangs:
        is_possible = True
        poses = []

        for dr, dc in boomerang:
            nr = r + dr
            nc = c + dc

            if (is_movable(nr, nc) and not visited[nr][nc]):
                poses.append((nr, nc))
            else: # 3좌표가 모두 가능해야함
                is_possible = False
                break

        if (is_possible):
            strength = 0
            
            for i in range(3): # 0이 center
                nr, nc = poses[i]
                visited[nr][nc] = True

                if (i == 0): # center
                    strength += board[nr][nc] * 2
                else:
                    strength += board[nr][nc]

            solve(idx+1, temp+strength)

            # 상태 복구 back
            for nr, nc in poses:
                visited[nr][nc] = False

    # 해당칸에 작업 안하고 넘어가는 경우
    solve(idx+1, temp)

solve(0, 0)
print(answer)

