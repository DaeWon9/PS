import sys
from collections import deque

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]

def is_finished(visited):
    for items in visited:
        for item in items:
            if item == False:
                return False
    return True

def check_area(board, visited, size):
    area_count = 0
    while not is_finished(visited):
        color_queue = deque()

        check = False
        for row in range(size):
            for col in range(size):
                if visited[row][col] == False:
                    color_queue.append((row, col, board[row][col]))
                    check = True
                    break
            if check:
                break

        while color_queue:
            row, col, color = color_queue.popleft()
            visited[row][col] = True
            for index in range(4):
                dc = col + direction_x[index]
                dr = row + direction_y[index]

                if (0 <= dc < size and 0 <= dr < size and board[dr][dc] == color and not visited[dr][dc]):
                    color_queue.appendleft((dr, dc, board[dr][dc]))

        area_count += 1

    return area_count


n = int(sys.stdin.readline())

picture_board = []
visited = [[False for _ in range(n)] for _ in range(n)]
picture_board_for_color_weakness = []
visited_for_color_weakness = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    input_string = sys.stdin.readline().rstrip()
    picture_board.append(list(map(str, input_string)))
    picture_board_for_color_weakness.append(list(map(str, input_string.replace("R", "G"))))

print(check_area(picture_board, visited, n), end=" ")
print(check_area(picture_board_for_color_weakness, visited_for_color_weakness, n))