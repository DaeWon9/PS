import sys
input = sys.stdin.readline

def solution(row):
    global answer
    for col in range(n):
        if(visited[col]):
            continue

        queen_pos_dict[row] = col
        if is_possible(row):
            if (row == n - 1):
                answer += 1
            else:
                visited[col] = True
                solution(row + 1)
                visited[col] = False

def is_possible(row):
    for prev_row in range(row):
        col_diff = abs(queen_pos_dict[row] - queen_pos_dict[prev_row])
        row_diff = row - prev_row
        # col check
        if (col_diff == 0):
            return False
        # cross check
        if (col_diff == row_diff):
            return False
    return True

n = int(input())
visited = [False for _ in range(n)]
queen_pos_dict = [0 for _ in range(n)]
answer = 0

solution(0)
print(answer)