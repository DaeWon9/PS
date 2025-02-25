import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < N)

def union():
    visited = [[False for _ in range(N)] for _ in range(N)]
    flag = False
    
    for row in range(N):
        for col in range(N):
            if (visited[row][col]):
                continue

            queue = deque()
            queue.append((row, col))
            visited[row][col] = True

            unioned_pos_list = [(row, col)]
            sum = board[row][col]

            while queue:
                r, c = queue.popleft()

                for i in range(4):
                    dr = r + direction_y[i]
                    dc = c + direction_x[i]

                    if (is_movable(dr, dc) and not visited[dr][dc]):
                        diff = abs(board[r][c] - board[dr][dc])

                        if (L <= diff <= R):
                            unioned_pos_list.append((dr, dc))
                            queue.append((dr, dc))
                            visited[dr][dc] = True
                            sum += board[dr][dc]
            
            count = len(unioned_pos_list)

            if (count == 1):
                continue
            
            updated_value = sum // count

            for rr, cc in unioned_pos_list:
                board[rr][cc] = updated_value
            
            flag = True
    
    return flag

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

N, L, R = map(int, input().split())
board = []
answer = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

while True:
    if (union()):
        answer += 1
    else:
        break

print(answer)