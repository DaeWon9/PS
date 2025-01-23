import sys
input = sys.stdin.readline

# 알고자하는 -> target을 좌측에 올려둔다고 상황을 가정
# 구슬을 놓을 수 있는 행위는 총 3가지 이다.
# 1. 아무 행위도 안한다
# 2. 좌측에 구슬을 추가한다.
# 3. 우측에 구슬을 추가한다. == 좌측에서 감소

def solve(cnt, weight):
    if (dp[cnt][weight]):  # 이미 확인
        return
    dp[cnt][weight] = True
    if (cnt == N):  # 모든 구슬을 확인한 경우
        return
    
    solve((cnt + 1), (weight))  # 아무 행위도 안 한다
    solve((cnt + 1), (weight + bead_list[cnt]))  # 좌측에 구슬 추가
    solve((cnt + 1), (weight - bead_list[cnt]))  # 우측에 구슬 추가

N = int(input())
bead_list = list(map(int, input().split()))

K = int(input())
target_list = list(map(int, input().split()))

# dp 배열 크기: 중심을 40000으로 설정 (최대 55000 범위)
OFFSET = 40000
MAX_WEIGHT = 15000  # 추가 가능한 최대 무게
dp = [[False for _ in range((OFFSET + MAX_WEIGHT + 1))] for _ in range(31)]

solve(0, OFFSET)  # 초기 중심값은 OFFSET으로 설정

for target in target_list:
    flag = False

    for j in range(1, (N + 1)):  # n회만에 target을 찾을 수 있나
        if ((0 <= (OFFSET + target) < len(dp[j])) and (dp[j][OFFSET + target])):
            flag = True
            break

    if (flag):
        print("Y", end=' ')
    else:
        print("N", end=' ')