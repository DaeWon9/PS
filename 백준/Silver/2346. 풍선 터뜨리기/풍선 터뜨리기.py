import sys
input = sys.stdin.readline

N  = int(input()) # 0은 없다
stack = list(enumerate(map(int, input().split())))
cur_idx = 0

while stack:
    num, move = stack.pop(cur_idx)
    print(num + 1, end= ' ')
    stack_len = len(stack)
    if (stack_len == 0):
        break

    if (move < 0):
        cur_idx = (cur_idx + move) % stack_len
    else:
        cur_idx = (cur_idx + move - 1) % stack_len
