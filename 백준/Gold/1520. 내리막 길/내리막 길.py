import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

def is_movable(dr, dc):
    return (0 <= dr < M and 0 <= dc < N)

def dfs(r, c):
    if (r == M-1 and c == N-1):
        return 1
    
    if (visit_count[r][c] != -1):
        return visit_count[r][c]

    count = 0
    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc) and graph[r][c] > graph[dr][dc]):
            count += dfs(dr, dc)
    
    visit_count[r][c] = count
    return visit_count[r][c]
    
M, N = map(int, input().split())
graph = []
visit_count = [[-1 for _ in range(N)] for _ in range(M)]

for _ in range(M):
    graph.append(list(map(int, input().split())))

print(dfs(0, 0))