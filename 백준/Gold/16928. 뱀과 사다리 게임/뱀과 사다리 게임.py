import sys
from collections import defaultdict, deque

snake_count, ladder_count = map(int, sys.stdin.readline().split())

snakes = defaultdict(int)
ladders = defaultdict(int)
count_board = [0] * 101
visited = [False] * 101

for _ in range(snake_count):
    start, finish = map(int, sys.stdin.readline().split())
    snakes[start] = finish

for _ in range(ladder_count):
    start, finish = map(int, sys.stdin.readline().split())
    ladders[start] = finish

position_queue = deque()
position_queue.append(1)

while position_queue:
    current_position = position_queue.popleft()

    if current_position == 100:  # finish
        print(count_board[current_position])
        break

    for dice_number in range(1, 7):
        moved_position = current_position + dice_number
        if 0 < moved_position < 101 and not visited[moved_position]:
            if moved_position in snakes.keys():
                moved_position = snakes[moved_position]

            if moved_position in ladders.keys():
                moved_position = ladders[moved_position]

            if not visited[moved_position]:
                visited[moved_position] = True
                count_board[moved_position] = count_board[current_position] + 1
                position_queue.append(moved_position)
