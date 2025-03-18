import sys
input = sys.stdin.readline

def solve(pivot_idx, count):
    global answer
    if (pivot_idx == N):
        answer = max(answer, count)
        return
    
    if eggs[pivot_idx][0] <= 0:
        solve(pivot_idx + 1, count)
        return

    is_any_hit = False 
    for next_idx in range(N):
        if (next_idx == pivot_idx or eggs[next_idx][0] <= 0):
            continue
        
        is_any_hit = True
        # 원래 값 저장
        pivot_dur, next_dur = eggs[pivot_idx][0], eggs[next_idx][0]

        eggs[pivot_idx][0] -= eggs[next_idx][1]
        eggs[next_idx][0] -= eggs[pivot_idx][1]

        new_count = count
        if (eggs[pivot_idx][0] <= 0):
            new_count += 1

        if (eggs[next_idx][0] <= 0):
            new_count += 1

        solve(pivot_idx + 1, new_count)

        # 백트랙킹
        eggs[pivot_idx][0], eggs[next_idx][0] = pivot_dur, next_dur

    if not is_any_hit:
        solve(pivot_idx + 1, count)

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
answer = 0

solve(0, 0)
print(answer)
