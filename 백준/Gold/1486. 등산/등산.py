import sys
import heapq
input = sys.stdin.readline

def get_adjusted_value(char):
    value = ord(char)
    return value - 6 if value >= 97 else value

def is_movable(r, c, dr, dc):
    return (0 <= dr < N and 0 <= dc < M and abs(get_adjusted_value(graph[r][c]) - get_adjusted_value(graph[dr][dc])) <= T)

def calc_move_time(prev_h, next_h):
    prev_value = get_adjusted_value(prev_h)
    next_value = get_adjusted_value(next_h)

    if (prev_value >= next_value):
        return 1
    return (prev_value - next_value) * (prev_value - next_value)

def get_shortest_time(row, col):
    tt = [[2147483647 for _ in range(M)] for _ in range(N)]
    tt[row][col] = 0

    h = [(0, row, col)]

    while h:
        t, r, c = heapq.heappop(h)

        if (tt[r][c] < t):
            continue

        for i in range(4):
            dr = r + direction_y[i]
            dc = c + direction_x[i]

            if (is_movable(r, c, dr, dc)):
                move_time = calc_move_time(graph[r][c], graph[dr][dc])
                updated_time = t + move_time

                if (tt[dr][dc] > updated_time):
                    tt[dr][dc] = updated_time

                    heapq.heappush(h, (updated_time, dr, dc))

    return tt[0][0]


direction_x = [0, 1, 0, -1]
direction_y = [-1, 0, 1, 0]


N, M, T, D = map(int, input().split())
times = [[2147483647 for _ in range(M)] for _ in range(N)]
times[0][0] = 0
heap =  [(0, 0, 0)] # time, row, col
graph = []

for _ in range(N):
    graph.append(input().rstrip())

while heap:
    t, r, c = heapq.heappop(heap)

    if (times[r][c] < t):
        continue

    for i in range(4):
        dr = r + direction_y[i]
        dc = c + direction_x[i]

        if (is_movable(r, c, dr, dc)):
            move_time = calc_move_time(graph[r][c], graph[dr][dc])
            updated_time = t + move_time

            if (times[dr][dc] > updated_time):
                times[dr][dc] = updated_time

                heapq.heappush(heap, (updated_time, dr, dc))

answer = 0

for row in range(N):
    for col in range(M):
        if (times[row][col] >= D):
            continue

        return_time = get_shortest_time(row, col)
        result_time = return_time + times[row][col]

        if (result_time <= D):
            height = get_adjusted_value(graph[row][col])
            if (answer < height):
                answer = height

print(answer - ord('A'))