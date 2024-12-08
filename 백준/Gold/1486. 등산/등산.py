import sys
import heapq
input = sys.stdin.readline

def get_adjusted_value(char):
    if (char.islower()):
        return ord(char) - ord('a') + 26
    return ord(char) - ord('A')

def is_movable(r, c, dr, dc):
    return (0 <= dr < N and 0 <= dc < M and abs(graph[r][c] - graph[dr][dc]) <= T)

def calc_move_time(prev_value, next_value, compare):
    if compare == 1:  # 오르막
        if (prev_value < next_value):
            return (next_value - prev_value) ** 2
        return 1
    else:  # 내리막
        if (prev_value > next_value):
            return (prev_value - next_value) ** 2
        return 1

direction_x = [0, 1, 0, -1]
direction_y = [-1, 0, 1, 0]

N, M, T, D = map(int, input().split())
times = [[2147483647 for _ in range(M)] for _ in range(N)]
times[0][0] = 0
heap =  [(0, 0, 0)] # time, row, col
graph = []

for _ in range(N):
    input_data = input().rstrip()
    row = []
    for data in input_data:
        row.append(get_adjusted_value(data))

    graph.append(row)

while heap:
    t, r, c = heapq.heappop(heap)

    if (times[r][c] < t):
        continue

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(r, c, dr, dc)):
            move_time = calc_move_time(graph[r][c], graph[dr][dc], 1)
            updated_time = t + move_time

            if (times[dr][dc] > updated_time):
                times[dr][dc] = updated_time

                heapq.heappush(heap, (updated_time, dr, dc))

times2 = [[2147483647 for _ in range(M)] for _ in range(N)]
times2[0][0] = 0
heap =  [(0, 0, 0)] # time, row, col

while heap:
    t, r, c = heapq.heappop(heap)

    if (times2[r][c] < t):
        continue

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(r, c, dr, dc)):
            move_time = calc_move_time(graph[r][c], graph[dr][dc], 2)
            updated_time = t + move_time

            if (times2[dr][dc] > updated_time):
                times2[dr][dc] = updated_time

                heapq.heappush(heap, (updated_time, dr, dc))

answer = 0
for row in range(N):
    for col in range(M):
        result_time = times[row][col] + times2[row][col]

        if (result_time <= D and answer < graph[row][col]):
            answer = graph[row][col]

print(answer)