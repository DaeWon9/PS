import sys
input = sys.stdin.readline

# 1~N 층까지 이용 가능
# K자리의 수가 보임.
# X층에 멈춰있음.
# 최소 1개 최대 P개 반전
N, K, P, X = map(int, input().split())
num_dict = dict()
num_dict[0] = [True, True, True, False, True, True, True]
num_dict[1] = [False, False, True, False, False, True, False]
num_dict[2] = [True, False, True, True, True, False, True]
num_dict[3] = [True, False, True, True, False, True, True]
num_dict[4] = [False, True, True, True, False, True, False]
num_dict[5] = [True, True, False, True, False, True, True]
num_dict[6] = [True, True, False, True, True, True, True]
num_dict[7] = [True, False, True, False, False, True, False]
num_dict[8] = [True, True, True, True, True, True, True]
num_dict[9] = [True, True, True, True, False, True, True]

converted_x = str(X).zfill(K)
pivot_status = []
for ch in converted_x:
    pivot_status.append((ch, num_dict[int(ch)]))

answer = 0

for target in range(1, N+1): # 1~N층 까지 탐색
    converted_target = str(target).zfill(K) # K자리로 표현
    target_status = [] # 타겟층의 상태
    for ch in converted_target:
        target_status.append((ch, num_dict[int(ch)]))
    
    cnt = 0
    for i in range(K): # K자리수만큼 돌면서 체크
        pivot_ = pivot_status[i]
        target_ = target_status[i]

        if (pivot_[0] == target_[0]): # 숫자가 같으면 다음 자릿수로 이동
            continue

        for j in range(7): # 숫자는 7칸으로 표시
            if (pivot_[1][j] != target_[1][j]):
                cnt += 1

            if (cnt > P):
                break
        if (cnt > P):
            break
        
    if (0 < cnt <= P):
        answer += 1

print(answer)