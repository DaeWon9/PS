import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < M):
        return True
    return False

N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
castle_info = [deque() for _ in range(P + 1)]
board = []

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

visited = [[False for _ in range(M)] for _ in range(N)]
answer = [0 for _ in range(P + 1)]

for r in range(N):
    input_data = list(map(str, list(input().rstrip())))
    for c in range(M):
        if (input_data[c] == '#'):
            continue
        elif (input_data[c] != '.'):
            castle_info[int(input_data[c])].append((r, c))
            visited[r][c] = True
            answer[int(input_data[c])] += 1

    board.append(input_data)

is_moved = True
while (is_moved):    
    is_moved = False
    for id in range(1, P + 1):
        
        if (not castle_info[id]):
            continue
        
        for _ in range(S[id]):    
            if (not castle_info[id]):
                break

            for _ in range(len(castle_info[id])):
                r, c = castle_info[id].popleft()

                for i in range(4):
                    dr = r + direction_y[i]
                    dc = c + direction_x[i]

                    if (is_movable(dr, dc) and board[dr][dc] == '.' and not visited[dr][dc]):
                        castle_info[id].append((dr, dc))
                        visited[dr][dc] = True
                        answer[id] += 1
                        is_moved = True
print(*answer[1:])