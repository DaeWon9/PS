import sys
input = sys.stdin.readline

# 열린문은 항상 두개..

def solve(idx, cnt, open1, open2):
    global answer
    if (idx == M):
        answer = min(answer, cnt)
        return
    
    target = nums[idx]
    
    # 이미 열려있는 경우
    if (target == open1 or target == open2):
        solve(idx + 1, cnt, open1, open2)
        return
    
    # open1을 target으로 이동
    solve(idx + 1, cnt + abs(target - open1), target, open2)
    # open2를 target으로 이동
    solve(idx + 1, cnt + abs(target - open2), open1, target)

N = int(input())
O1, O2 = map(int, input().split())
M = int(input())
answer = float('inf')

nums = [int(input()) for _ in range(M)]

solve(0, 0, O1, O2)
print(answer)