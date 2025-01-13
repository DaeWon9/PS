import sys
input = sys.stdin.readline

N, L = map(int, input().split())
answer = 0
board = []

for _ in range(N):
    input_data = list(map(int, input().split()))
    board.append(input_data)

    prev_num = input_data[0]
    dup_count = 1
    inclination = 0
    flag = True
    check_next_dup_count = False

    for i in range(1, N):
        cur_num = input_data[i]
        diff = prev_num - cur_num

        if (diff > 1 or diff < -1): # 두칸 이상 차이나면 불가
            flag = False
            break
        
        if (diff == 0):
            dup_count += 1
            if (check_next_dup_count and dup_count >= L):
                dup_count = 0
                check_next_dup_count = False
            continue

        inclination = -diff
        prev_num = cur_num

        if (check_next_dup_count):
            if (dup_count < L):
                flag = False
                break
            else:
                dup_count = 0
                check_next_dup_count = False

        if (inclination > 0): # 다음이 경사가 더 높음
            if (dup_count >= L): # 경사로를 놓을 수 있음
                dup_count = 1
                continue
            else:
                flag = False
                break
        else: # 다음이 경사가 낮음
            check_next_dup_count = True
            dup_count = 1

            if (dup_count >= L):
                dup_count = 0
                check_next_dup_count = False

    if (check_next_dup_count and dup_count < L):
        flag = False

    if (flag):
        answer += 1

if (N == 1):
    print(1)
    exit(0)

for c in range(N):
    prev_num = board[0][c]
    dup_count = 1
    inclination = 0
    flag = True
    check_next_dup_count = False

    for r in range(1, N):
        cur_num = board[r][c]
        diff = prev_num - cur_num

        if (diff > 1 or diff < -1): # 두칸 이상 차이나면 불가
            flag = False
            break
        
        if (diff == 0):
            dup_count += 1

            if (check_next_dup_count and dup_count >= L):
                if (dup_count >= L):
                    dup_count = 0
                    check_next_dup_count = False
            continue

        inclination = -diff
        prev_num = cur_num

        if (check_next_dup_count):
            if (dup_count < L):
                flag = False
                break
            else:
                dup_count = 0
                check_next_dup_count = False

        if (inclination > 0): # 다음이 경사가 더 높음
            if (dup_count >= L): # 경사로를 놓을 수 있음
                dup_count = 1
                continue
            else:
                flag = False
                break
        else: # 다음이 경사가 낮음
            check_next_dup_count = True
            dup_count = 1

            if (dup_count >= L):
                dup_count = 0
                check_next_dup_count = False

    if (check_next_dup_count and dup_count < L):
        flag = False
        
    if (flag):
        answer += 1

print(answer)