import sys
from collections import deque
input = sys.stdin.readline

def is_movable(dr, dc):
    return (0 <= dr < N and 0 <= dc < M)

def check_right_side(r, c):
    count = 1

    for i in range(1, K):
        dc = c + i
        if (is_movable(r, dc) and board[r][dc] == 1):
            count += 1
        else:
            break
    
    return (count == K)

def check_down_side(r, c):
    count = 1

    for i in range(1, K):
        dr = r + i
        if (is_movable(dr, c) and board[dr][c] == 1):
            count += 1
        else:
            break
    
    return (count == K)

def print_answer(): # case1 != case2
    check_set = set()
    result = []
    r1, c1, case1 = answer[0]
    r2, c2, case2 = answer[1]

    if (case1 == 'right'):
        for i in range(K):
            check_set.add((r1, c1+i))
    else:
        for i in range(K):
            check_set.add((r1+i, c1))

    if (case2 == 'right'):
        for i in range(K):
            if ((r2, c2+i) in check_set):
                result.append((r2+1, c2+i+1))
    else:
        for i in range(K):
            if ((r2+i, c2) in check_set):
                result.append((r2+i+1, c2+1))

    print(len(result))
    for ans in result:
        print(*ans)

N, M, K = map(int, input().split())
board = []
queue = deque()
answer = []

for r in range(N):
    input_data = list(map(int, input().split()))

    for c in range(M):
        if (input_data[c] == 1):
            queue.append((r, c))

    board.append(input_data)

while (queue and len(answer) < 4):
    r, c = queue.popleft()

    right_side = check_right_side(r, c)
    if (right_side):
        answer.append((r, c, 'right'))

    if (K != 1):
        down_side = check_down_side(r, c)
        if (down_side):
            answer.append((r, c, 'down'))

if (len(answer) == 1):
    print(K)
    if (answer[0][2] == 'right'):
        for i in range(K):
            print(answer[0][0]+1, answer[0][1]+i+1)
    else:
        for i in range(K):
            print(answer[0][0]+i+1, answer[0][1]+1)
elif (len(answer) == 4):
    print(0)
else: # len: 2
    print_answer()