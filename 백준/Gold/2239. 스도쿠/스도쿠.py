import sys
input = sys.stdin.readline

def solve(idx):
    if (idx == len(empty_poses)):
        for row in board:
            print("".join(map(str, row)))
        exit(0)

    r, c = empty_poses[idx]
    rect_idx = pos_to_rect_idx[(r, c)]
    possible_nums = sorted(rows[r] & cols[c] & rects[rect_idx])
    
    for num in possible_nums:
        board[r][c] = num
        rows[r].remove(num)
        cols[c].remove(num)
        rects[rect_idx].remove(num)

        solve(idx + 1)

        board[r][c] = 0
        rows[r].add(num)
        cols[c].add(num)
        rects[rect_idx].add(num)


pos_to_rect_idx = {(r, c): (r//3)*3 + (c//3) for r in range(9) for c in range(9)}

rows = [set(range(1, 10)) for _ in range(9)]
cols = [set(range(1, 10)) for _ in range(9)]
rects = [set(range(1, 10)) for _ in range(9)]

empty_poses = []
board = [[] for _ in range(9)]

for r in range(9):
    row = input().rstrip()
    for c in range(9):
        val = int(row[c])
        if (val == 0):
            empty_poses.append((r, c))
        else:
            rows[r].remove(val)
            cols[c].remove(val)
            rects[pos_to_rect_idx[(r, c)]].remove(val)
        board[r].append(val)

solve(0)
