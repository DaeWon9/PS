import sys
input = sys.stdin.readline

# 2 ≤ N ≤ 100,000
def flip(s, i):
    s[i] = not s[i]
    if (i == 0):
        s[1] = not s[1]
        return
    
    if (i == N-1):
        s[i-1] = not s[i-1]
        return
    
    s[i-1] = not s[i-1]
    s[i+1] = not s[i+1]
    return

N = int(input())
case_1 = [False for _ in range(N)]
goal = [False for _ in range(N)]

for i, d in enumerate(input().rstrip()):
    if (d == '1'):
        case_1[i] = True

for i, d in enumerate(input().rstrip()):
    if (d == '1'):
        goal[i] = True

case_2 = case_1[:]

case_1_cnt = 1
case_2_cnt = 0

# case_1 첫 번째 스위치를 누르고 시작
flip(case_1, 0)
for i in range(1, N):
    # i-1 번째의 스위치는 i번째에서 결정남
    if (case_1[i-1] != goal[i-1]):
        flip(case_1, i)
        case_1_cnt += 1

# case_2 첫 번째 스위치를 누르지 않고 시작
for i in range(1, N):
    if (case_2[i-1] != goal[i-1]):
        flip(case_2, i)
        case_2_cnt += 1

answer = float('inf')

if (case_1[-1] == goal[-1]):
    answer = min(answer, case_1_cnt)

if (case_2[-1] == goal[-1]):
    answer = min(answer, case_2_cnt)

if (answer == float('inf')):
    print(-1)
else:
    print(answer)