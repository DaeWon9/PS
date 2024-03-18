import sys
import heapq
input = sys.stdin.readline

def is_movable(dr, dc):
    if (0 <= dr < N and 0 <= dc < M):
        return True
    return False

direction_x = [1, -1, 0, 0]
dircetion_y = [0, 0, 1, -1]

N, M = map(int, input().split())
board = []
garbage_pos_set = set()
garbage_nearby_set = set()
flower_pos = ()
start_pos = ()

vistied = [[False for _ in range(M)] for _ in range(N)]

for r in range(N):
    input_data = list(input().rstrip())

    for c in range(M):
        if (input_data[c] == 'F'):
            flower_pos = (r, c)
            input_data[c] = '.'
        elif (input_data[c] == 'S'):
            start_pos = (r, c)
            input_data[c] = '.'
        elif (input_data[c] == 'g'):
            garbage_pos_set.add((r, c))
            for i in range(4):
                garbage_nearby_set.add((r + dircetion_y[i], c + direction_x[i]))
    
    board.append(input_data)

heap = [[0, 0, start_pos[0], start_pos[1]]]
vistied[start_pos[0]][start_pos[1]] = True

while heap:
    cnt1, cnt2, r, c = heapq.heappop(heap)

    for i in range(4):
        dr = r + dircetion_y[i]
        dc = c + direction_x[i]

        if (is_movable(dr, dc) and not vistied[dr][dc]):
            if (board[dr][dc] == '.'):
                if ((dr, dc) == flower_pos):
                    print(cnt1, cnt2)
                    exit(0)

                if ((dr, dc) in garbage_nearby_set):
                    heapq.heappush(heap, (cnt1, cnt2 + 1, dr, dc))
                else:
                    heapq.heappush(heap, (cnt1, cnt2, dr, dc))
            elif (board[dr][dc] == 'g'):
                heapq.heappush(heap, (cnt1 + 1, cnt2, dr, dc))

            vistied[dr][dc] = True